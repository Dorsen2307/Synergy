class Bank:
    __money = 0

    def __init__(self, money):
        self.__money = money

    def get_money(self):
        return self.__money

    def top_up(self, x):
        """Пополняет кассу деньгами"""
        self.__money += x

    def count_1000(self):
        """Выводит сколько целых тысяч осталось в кассе"""
        print(f"В кассе осталось {self.__money // 1000} целых тысяч.")

    def take_away(self, x):
        """Забрать деньги из кассы или сообщить, что денег недостаточно"""
        if x >= self.__money:
            print("Не достаточно денег!")
        else:
            self.__money -= x

bank = Bank(100000)

# пополним кассу на 15000
bank.top_up(15000)
print(f"В кассе {bank.get_money()}")

# снимем деньги из кассы
bank.take_away(12300)
print(f"В кассе {bank.get_money()}")

# посмотрим сколько целых тысяч осталось в банке
bank.count_1000()
