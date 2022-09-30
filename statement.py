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

    for perf in invoice['performances']:
        performance = Performance(perf)
        play = plays[performance.play_id()]
        this_amount = performance.amount(play)
        performance_credits = performance.credits(play)

        line = f' {play["name"]}: {format_as_dollars(this_amount.current() / 100)} ({performance.audience()} seats)\n'
        printer.print(line)

        invoice_amount = invoice_amount.add(this_amount)
        volume_credits = volume_credits.add(performance_credits)

    printer.print(f'Amount owed is {format_as_dollars(invoice_amount.current() // 100)}\n')
    printer.print(f'You earned {volume_credits.current()} credits\n')

    return printer.output()
