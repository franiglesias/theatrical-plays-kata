import math

from domain.amount import Amount
from domain.credits import Credits
from domain.performance import Performance
from domain.printer import Printer


def statement(invoice, plays):
    printer = Printer()
    invoice_amount = Amount(0)
    volume_credits = Credits(0)
    printer.print(f'Statement for {invoice["customer"]}\n')

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    def calculate_performance_amount(play, performance):
        if play['type'] == "tragedy":
            return performance.calculate_amount_for_tragedy()
        if play['type'] == "comedy":
            return performance.calculate_amount_for_comedy()

        raise ValueError(f'unknown type: {play["type"]}')

    def calculate_performance_credits(perf, play):
        return Credits(max(perf['audience'] - 30, 0)). \
            add(extra_volume_credits_for_comedy(perf, play))

    def extra_volume_credits_for_comedy(perf, play):
        if "comedy" != play["type"]:
            return Credits(0)

        return Credits(math.floor(perf['audience'] / 5))

    for perf in invoice['performances']:
        performance = Performance(perf)
        play = plays[performance.play_id()]
        this_amount = calculate_performance_amount(play, performance)
        performance_credits = calculate_performance_credits(perf, play)

        line = f' {play["name"]}: {format_as_dollars(this_amount.current() / 100)} ({performance.audience()} seats)\n'
        printer.print(line)

        invoice_amount = invoice_amount.add(this_amount)
        volume_credits = volume_credits.add(performance_credits)

    printer.print(f'Amount owed is {format_as_dollars(invoice_amount.current() // 100)}\n')
    printer.print(f'You earned {volume_credits.current()} credits\n')

    return printer.output()
