import math

from domain.amount import Amount


def statement(invoice, plays):
    total_amount = 0
    invoice_amount = Amount(0)
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    def calculate_performance_amount(perf, play):
        if play['type'] == "tragedy":
            return calculate_amount_for_tragedy(perf)
        if play['type'] == "comedy":
            return calculate_amount_for_comedy(perf)

        raise ValueError(f'unknown type: {play["type"]}')

    def calculate_amount_for_comedy(perf):
        amount = 30000
        amount += extra_amount_for_high_audience_in_comedy(perf)
        amount += 300 * perf['audience']
        return amount

    def extra_amount_for_high_audience_in_comedy(perf):
        if perf['audience'] <= 20:
            return 0

        return 10000 + 500 * (perf['audience'] - 20)

    def calculate_amount_for_tragedy(perf):
        amount = 40000
        amount += extra_amount_for_high_audience_in_tragedy(perf)
        return amount

    def extra_amount_for_high_audience_in_tragedy(perf):
        if perf['audience'] <= 30:
            return 0

        return 1000 * (perf['audience'] - 30)

    def calculate_performance_credits(perf, play):
        # add volume credits
        credits = max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        credits += extra_volume_credits_for_comedy(perf, play)
        return credits

    def extra_volume_credits_for_comedy(perf, play):
        if "comedy" != play["type"]:
            return 0

        return math.floor(perf['audience'] / 5)

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        this_amount = calculate_performance_amount(perf, play)
        performance_credits = calculate_performance_credits(perf, play)
        line = f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'

        result += line
        total_amount += this_amount
        invoice_amount = invoice_amount.add(Amount(this_amount))
        volume_credits += performance_credits

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result
