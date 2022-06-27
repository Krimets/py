# class MoneyBox. Копилка.

class MoneyBox:
    def __init__(self, capacity=0):
        self.capacity = capacity  # конструктор с аргументом – вместимость копилки
        print(f'Всего места в копилке для {capacity} монет')
    def can_add(self, v):
        if (self.capacity - v) < 0:
            print(f'Увы, для {v} монет места в копилке нет, а места осталось для {self.capacity} монет')
            return False
        else:
            print(f'Ещё есть место, {v} монет поместится')
            return True
    def add(self, v):
        if self.can_add(v) == True:  # проверить сколько влезет
            self.capacity -= v  # положить v монет в копилку
            print(f'Осталось места для {self.capacity} монет')
        else:
            return f'Увы, столько места в копилке нет, а места осталось для {self.capacity} монет'
x = MoneyBox(9)
x.add(5)
x.can_add(2)
x.add(9)
