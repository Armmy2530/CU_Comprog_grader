class BigWallet:
    def __init__(self, NOTES):
        self.notes = NOTES
        self.balance = 0

    def valid_note(self, v):
        return v in self.notes

    def add(self, v, n):
        if not self.valid_note(v):
            return
        else:
            self.balance += v*n

    def total(self):
        return self.balance

    def __lt__ (self, rhs):
        return self.total() < rhs.total()
