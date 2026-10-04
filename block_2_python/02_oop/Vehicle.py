class Vehicle:
    """Главный класс транспорта.
    
    Args:
        make (str): Марка.
        model (str): Модель.
        year (int): Год производства.
        price (int): Цена.
    """
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        """Выводит информацию о транспорте."""
        print(
            f"Марка: {self.make}"
            f"\nМодель: {self.model}"
            f"\nГод выпуска: {self.year}"
            f"\nСтоимость: {self.price} руб"
        )


class Car(Vehicle):
    """Класс, представляющий машину.
    
    Args:
        make (str): Марка.
        model (str): Модель.
        year (int): Год производства.
        price (int): Цена.
        num_doors (int): Количество дверей. 
        body_style (str): Тип кузова.
    """
    def __init__(self, make, model, year, price, num_doors, body_style):
        super().__init__(make, model, year, price)
        self.num_doors = num_doors
        self.body_style = body_style


class Truck(Vehicle):
    """Класс, представляющий грузовик.
    
    Args:
        make (str): Марка.
        model (str): Модель.
        year (int): Год производства.
        price (int): Цена.
        bed_length (int): Длина кузова. 
        towing_capacity (str): Грузоподъемность.
    """
    def __init__(self, make, model, year, price, bed_length, towing_capacity):
        super().__init__(make, model, year, price)
        self.bed_length = bed_length
        self.towing_capacity = towing_capacity


car = Car("Toyota", "Camry", 2022, 2900000, 4, "седан")

truck = Truck("Ford", "F-MAX", 2023, 6000000, 6162, "13т")

car.display_info()
truck.display_info()
