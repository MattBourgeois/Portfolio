class monthly_budget:
    def __init__(self, pay, saving, bill, free):
        self.pay = pay
        self.saving = saving
        self.bill = bill
        self.free = free
    def bills(self):
        if self.pay > self.bill:
            k = (self.bill/self.pay) * 100
            j = round(k)
            print(str(j) + str("%"))
        elif self.pay < self.bill:
            print("Insufficant Funds")
    def sav(self):
        if self.pay > self.saving:
            x = (self.saving/self.pay) * 100
            y = round(x)
            print(str(y) + str("%"))
    def extra(self):
        if self.pay > self.free:
            b = (self.free/self.saving)
            c = round(b)
            print(str(c) + str("%"))
    def leftover(self):
        if self.pay > 0:
            afterbill = self.pay - self.bill
            left = afterbill - self.saving
            print(str("$") + str(left))

matt_may = monthly_budget(3118, 675,  1454, 300)

matt_may.bills()
matt_may.sav()
matt_may.extra()
matt_may.leftover()
