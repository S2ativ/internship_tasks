class Confectionary:
    """Главный класс десертов.
    
    Args:
        name (str): Название.
        price (int): Цена.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        """Текстовое описание десерта."""
        print(f"{self.name} по цене {self.price} руб/кг")


class Cake(Confectionary):
    """Класс торта."""
    def describe(self):
        """Текстовое описание торта."""
        print(f"{self.name} торт стоит {self.price} руб/кг")


class Candy(Confectionary):
    """Класс конфет."""
    def describe(self):
        """Текстовое описание конфет."""
        print(f"{self.name} конфеты стоимостью {self.price} руб/кг")


class Cookie(Confectionary):
    """Класс печенья."""
    pass


cake = Cake("Пражский", 1200)
candy = Candy("Шоколадные динозавры", 560)
cookie = Cookie("Овсяное печенье с миндалем", 250)

cake.describe()
candy.describe()
cookie.describe()
