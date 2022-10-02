from domain.amount import Amount
from domain.credits import Credits
from domain.performance import Performances
from domain.play import Plays
from domain.printer import Printer


def statement(invoice, plays):
    printer = Printer()
    invoice_amount = Amount(0)
    volume_credits = Credits(0)
    performances = Performances(invoice['performances'], Plays(plays))

    printer.print(f'Statement for {invoice["customer"]}\n')

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for performance in performances:
        this_amount = performance.amount()
        performance_credits = performance.credits()

        line = f' {performance.play().name()}: {format_as_dollars(this_amount.current() / 100)} ({performance.audience()} seats)\n'
        printer.print(line)

        invoice_amount = invoice_amount.add(this_amount)
        volume_credits = volume_credits.add(performance_credits)

    printer.print(f'Amount owed is {format_as_dollars(invoice_amount.current() // 100)}\n')
    printer.print(f'You earned {volume_credits.current()} credits\n')

    return printer.output()
