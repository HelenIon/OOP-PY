# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Wizard:
    def __init__(self, name: str, mana_amount: int, damage: float):
        """
                Создание и подготовка к работе объекта "Маг"
                :param name: Имя мага
                :param mana_amount: Количество маны мага
                :param damage: Наносимый магом урон

                Примеры:
                >>> wizard = Wizard("Олег", 500, 15.7)  # инициализация экземпляра класса
        """

        self.name = name
        self.mana_amount = mana_amount
        self.damage = damage

        if not isinstance(name, str):
            raise TypeError("Имя должно иметь строковое значение")
        self.name = name

        if not isinstance(mana_amount, int):
            raise TypeError("Количество маны должно иметь тип int")
        if mana_amount <= 0:
            raise ValueError("Количество маны должно быть положительным числом")
        self.mana_amount = mana_amount

        if not isinstance(damage, (int, float)):
            raise TypeError("Урон должен иметь тип int или float")
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным числом")
        self.damage = damage

    def cast_fireball(self, aim):
        """
            Функция, наносящая урон заклинанием огненного шара по цели.

            :param aim: Цель, на которую накладывается заклинание

            Примеры:
            >>> wizard = Wizard("Олег", 500, 15.7)
            >>> wizard.cast_fireball("Вася")
            Вася получил 15.7 ед. урона от файрбола персонажа Олег
        """

        print("{0} получил {1} ед. урона от файрбола персонажа {2}".
              format(aim, self.damage, self.name))


    def spend_mana(self, req_mana_amount: int) -> None:
        """
            Функция, уменьшающая количество маны у мага

            :param req_mana_amount: Количество маны, которое будет потрачено магом

            :raise ValueError: Если затрачиваемое количество маны
                имеет отрицательное значение, то вызываем ошибку

            Примеры:
            >>> wizard = Wizard("Олег", 500, 15.7)
            >>> wizard.spend_mana(10)
        """

        if not isinstance(req_mana_amount, int):
            raise TypeError("Количество маны должно иметь тип int")
        if req_mana_amount <= 0:
            raise ValueError("Количество маны должно быть положительным числом")


class Warrior:
    def __init__(self, name: str, stamina_amount: int, damage: float):
        """
                Создание и подготовка к работе объекта "Воин"
                :param name: Имя война
                :param stamina_amount: Количество единиц выносливости война
                :param damage: Наносимый войном урон

                Примеры:
                >>> warrior = Warrior("Антон", 240, 8.4)  # инициализация экземпляра класса
        """

        self.name = name
        self.stamina_amount = stamina_amount
        self.damage = damage

        if not isinstance(name, str):
            raise TypeError("Имя должно иметь строковое значение")
        self.name = name

        if not isinstance(stamina_amount, int):
            raise TypeError("Выносливость должна иметь тип int")
        if stamina_amount <= 0:
            raise ValueError("Выносливость должна быть положительным числом")
        self.stamina_amount = stamina_amount

        if not isinstance(damage, (int, float)):
            raise TypeError("Урон должен иметь тип int или float")
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным числом")
        self.damage = damage

    def sword_hit(self, aim):
        """
            Функция, наносящая урон мечом по цели.

            :param aim: Цель, принимающая урон мечом

            Примеры:
            >>> warrior = Warrior("Антон", 240, 8.4)
            >>> warrior.sword_hit("Ваня")
            Антон бьет мечом персонажа по имени Ваня
        """

        print(self.name + " бьет мечом персонажа по имени " + aim)

    def get_hero_info(self):
        """
            Функция, выводящая на экран всю информацию о персонаже

            Примеры:
            >>> warrior = Warrior("Антон", 240, 8.4)
            >>> warrior.get_hero_info()
            Имя:            Антон
            Класс:          Воин
            Выносливость:   240 ед.
        """

        print("Имя:\t\t\t{0}\nКласс:\t\t\tВоин\nВыносливость:\t{1} ед.".
              format(self.name, self.stamina_amount))


class Thief:
    def __init__(self, name: str, sneak: int, damage: float):
        """
                Создание и подготовка к работе объекта "Вор"
                :param name: Имя вора
                :param sneak: Уровень скрытности вора
                :param damage: Наносимый вором урон

                Примеры:
                >>> thief = Thief("Grey fox", 320, 5.6)  # инициализация экземпляра класса
        """
        self.name = name
        self.sneak = sneak
        self.damage = damage

        if not isinstance(name, str):
            raise TypeError("Имя должно иметь строковое значение")
        self.name = name

        if not isinstance(sneak, int):
            raise TypeError("Скрытность должна иметь тип int")
        if sneak <= 0:
            raise ValueError("Скрытность должна быть положительным числом")
        self.sneak = sneak

        if not isinstance(damage, (int, float)):
            raise TypeError("Урон должен иметь тип int или float")
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным числом")
        self.damage = damage

    def dagger_hit(self, aim):
        """
            Функция, наносящая урон кинжалом по цели.

            :param aim: Цель, принимающая урон кинжалом

            Примеры:
            >>> thief = Thief("Grey fox", 320, 5.6)
            >>> thief.dagger_hit("Бродяга")
            Grey fox ударил в спину персонажа по имени Бродяга
        """

        print(self.name + " ударил в спину персонажа по имени " + aim)

    def pickpocket(self, hero_name: str, subject_name: str):
        """
            Функция, осуществляющая карманную кражу предмета у определенного персонажа.

            :param hero_name: Цель, у которой производится кража
            :param subject_name: Предмет, который необходимо своровать

            Примеры:
            >>> thief = Thief("Grey fox", 320, 5.6)
            >>> thief.pickpocket("Олег", "Посох крутости")
            Grey fox украл Посох крутости из кармана персонажа по имени Олег
        """

        if not isinstance(hero_name, str):
            raise TypeError("Имя должно иметь строковое значение")
        if not isinstance(subject_name, str):
            raise TypeError("Название предмета должно иметь строковое значение")

        print("{0} украл {1} из кармана персонажа по имени {2}".
              format(self.name, subject_name, hero_name))


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
