class Bank:
    __money = 0

    def __init__(self, money):
        self.__money = money

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