from domain.invoice import Invoice
from domain.printer import Printer


def statement(invoice_data, plays):
    def formatted_line(title, audience, amount):
        return f' {title}: {format_as_dollars(amount.current() / 100)} ({audience} seats)\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    printer = Printer()

    invoice = Invoice(invoice_data, plays)

    printer.print(f'Statement for {invoice.customer()}\n')
    for performance in invoice.performances():
        printer.print(formatted_line(performance.title(), performance.audience(), performance.amount()))
    printer.print(f'Amount owed is {format_as_dollars(invoice.amount().current() // 100)}\n')
    printer.print(f'You earned {invoice.credits().current()} credits\n')

    return printer.output()
