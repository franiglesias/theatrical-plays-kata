from domain.amount import Amount


class Audience:
    def __init__(self, audience):
        self.audience = audience

    def amount(self, threshold, minimum, coeficient):
        if self.audience <= threshold:
            return Amount(0)

        return Amount(minimum + coeficient * (self.audience - threshold))
