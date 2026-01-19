from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass


class Coffee(Beverage):
    def get_description(self):
        return "Кафе"

    def cost(self):
        return 2.00


class DecafCoffee(Beverage):
    def get_description(self):
        return "Безкофеиново кафе"

    def cost(self):
        return 2.50


class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @abstractmethod
    def get_description(self):
        pass


class Cream(BeverageDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", сметана"

    def cost(self):
        return self._beverage.cost() + 0.50


class VeganCream(BeverageDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", веган сметана"

    def cost(self):
        return self._beverage.cost() + 0.70


class CowMilk(BeverageDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", краве мляко"

    def cost(self):
        return self._beverage.cost() + 0.60


class SoyMilk(BeverageDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", соево мляко"

    def cost(self):
        return self._beverage.cost() + 0.80


class CoconutMilk(BeverageDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", кокосово мляко"

    def cost(self):
        return self._beverage.cost() + 1.00


class AlmondMilk(BeverageDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", бадемово мляко"

    def cost(self):
        return self._beverage.cost() + 1.20


class Cinnamon(BeverageDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", канела"

    def cost(self):
        return self._beverage.cost() + 0.40


def main():
    print("=== Гурме кафе меню ===")

    drink1 = Cream(Cinnamon(Coffee()))
    print(f"{drink1.get_description()} -> {drink1.cost():.2f} лв.")

    drink2 = AlmondMilk(DecafCoffee())
    print(f"{drink2.get_description()} -> {drink2.cost():.2f} лв.")

    drink3 = VeganCream(Cinnamon(CoconutMilk(Coffee())))
    print(f"{drink3.get_description()} -> {drink3.cost():.2f} лв.")


if __name__ == "__main__":
    main()