from domain.invoice import Invoice
from domain.statement_printer import StatementPrinter
from infrastructure.console_printer import ConsolePrinter


def statement(invoice_data, plays):
    invoice = Invoice(invoice_data, plays)
    statement_printer = StatementPrinter(ConsolePrinter())
    invoice.fill(statement_printer)

    return statement_printer.print()
