from domain.amount import Amount
from domain.credits import Credits
from domain.invoice import Invoice
from domain.printer import Printer


def statement(invoice_data, plays):
    printer = Printer()
    invoice_amount = Amount(0)
    volume_credits = Credits(0)
    invoice = Invoice(invoice_data, plays)

    printer.print(f'Statement for {invoice.customer()}\n')

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    def formatted_line(title, audience, amount):
        return f' {title}: {format_as_dollars(amount.current() / 100)} ({audience} seats)\n'

    for performance in invoice.performances():
        printer.print(formatted_line(performance.title(), performance.audience(), performance.amount()))
        invoice_amount = invoice_amount.add(performance.amount())
        volume_credits = volume_credits.add(performance.credits())

    printer.print(f'Amount owed is {format_as_dollars(invoice_amount.current() // 100)}\n')
    printer.print(f'You earned {volume_credits.current()} credits\n')

    return printer.output()
