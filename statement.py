import math

from domain.amount import Amount


def statement(invoice, plays):
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
        return Amount(30000)\
            .add(Amount(extra_amount_for_high_audience_in_comedy(perf)))\
            .add(Amount(300 * perf['audience']))\
            .current()

    def extra_amount_for_high_audience_in_comedy(perf):
        if perf['audience'] <= 20:
            return Amount(0).current()

        return Amount(10000 + 500 * (perf['audience'] - 20)).current()

    def calculate_amount_for_tragedy(perf):
        return Amount(40000)\
            .add(Amount(extra_amount_for_high_audience_in_tragedy(perf)))\
            .current()


    def extra_amount_for_high_audience_in_tragedy(perf):
        if perf['audience'] <= 30:
            return Amount(0).current()

        return Amount(1000 * (perf['audience'] - 30)).current()

    def calculate_performance_credits(perf, play):
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
        invoice_amount = invoice_amount.add(Amount(this_amount))
        volume_credits += performance_credits

    result += f'Amount owed is {format_as_dollars(invoice_amount.current()//100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result
