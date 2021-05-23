class buy:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Две клетки - хорошо, а одна большая - лучше! Размер клетки равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клеточка стала меньше, теперь она равна: {sub} клеточкам' if sub > 0 else 'Клетка исчезла :('

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


buy = buy(24)
buy_2 = buy(2)
print(buy + buy_2)
print(buy - buy_2)
print(buy / buy_2)
print(buy * buy_2)
print(buy.make_order(7))