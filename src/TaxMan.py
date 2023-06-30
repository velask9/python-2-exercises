class TaxMan:

    def __init__(self, items, tax):
        self.items = items
        self.tax = tax

    def calc_total(self):
        total = sum(item["price"] for item in self.items)
        return total

    def get_total(self):
        total = self.calc_total()
        tax_percentage = float(self.tax.strip('%')) / 100
        tax_amount = total * tax_percentage
        total_with_tax = total + tax_amount
        return total_with_tax


items = [
    {"id": 1, "desc": "clock", "price": 1.00},
    {"id": 2, "desc": "socks", "price": 2.00},
    {"id": 3, "desc": "razor", "price": 3.00},
]

# tm = TaxMan(items, "10%")
# total_with_tax = tm.get_total()
# print(total_with_tax)
