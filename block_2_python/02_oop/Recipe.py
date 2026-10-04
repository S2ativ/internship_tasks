from abc import ABC, abstractmethod


class Recipe(ABC):
    """Абстрактный базовый класс для рецептов."""

    @abstractmethod
    def cook(self):
        """Описывает процесс приготовления.
        
        Метод обязателен к переопределению во всех дочерних классах.
        """
        pass


class Entree(Recipe):
    """Класс основного блюда.

    Args:
        ingredients (list): Список ингредиентов.
    """

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def cook(self):
        """Выводит текстовое описание процесса приготовления основного блюда."""
        print(
            f"Готовим на медленном огне смесь ингредиентов({', '.join(self.ingredients)}) для основного блюда"
        )


class Dessert(Recipe):
    """Класс десерта.

    Args:
        ingredients (list): Список ингредиентов.
    """

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def cook(self):
        """Выводит текстовое описание процесса приготовления десерта."""
        print(f"Смешиваем {', '.join(self.ingredients)} для десерта")


class Appetizer(Recipe):
    """Класс закуски.
    
    Является абстрактным промежуточным классом, так как метод cook в нем не переопределен.
    """
    pass


class PartyMix(Appetizer):
    """Класс снеков."""

    def cook(self):
        """Выводит текстовое описание процесса подготовки снеков."""
        print("Готовим снеки - выкладываем на поднос орешки, чипсы и крекеры")


# Проверка работы:
entree = Entree(["курица", "рис", "овощи"])
dessert = Dessert(["мороженое", "шоколадные чипсы", "мараскиновые вишни"])
partymix = PartyMix()

entree.cook()
dessert.cook()
partymix.cook()