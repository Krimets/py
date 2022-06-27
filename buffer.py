# Buffer. Сумма 5 последующих чисел
class Buffer:
    def __init__(self):
        self.d = []  # пустой список
    def add(self, *a):  # получаем список чисел
        for i in a:
            self.d.append(i)  # прибавляем числа к списку
            if len(self.d) == 5:  # пока их не станет 5
                print(sum(self.d))  # выводим сумму 5 чисел
                self.d = []
    def get_current_part(self):  # вернуть сохраненные в текущий момент элементы
        print(self.d)            # последовательности в порядке, в котором они были добавлены


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part()  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part()  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()  # вернуть [1]
