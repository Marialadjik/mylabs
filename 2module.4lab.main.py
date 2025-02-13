class Tree: #базовый класс
    """
    Базовый класс для всех деревьев.

    Attributes:
        species (str): Вид дерева.
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.
    """

    def __init__(self, species: str, height: float, age: int) -> None:
        """
        Инициализация дерева.

        Args:
            species (str): Вид дерева.
            height (float): Высота дерева в метрах.
            age (int): Возраст дерева в годах.
        """
        self._species = species  # Инкапсулированный атрибут, чтобы предотвратить случайное изменение
        self._height = height  # Инкапсулированный атрибут, чтобы высота дерева не была изменена напрямую
        self._age = age  # Инкапсулированный атрибут, чтобы возраст дерева не был изменен напрямую

    def __str__(self) -> str:
        """Возвращает строковое представление дерева."""
        return f"{self._species} tree, {self._height}m tall, {self._age} years old"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление дерева."""
        return f"Tree(species='{self._species}', height={self._height}, age={self._age})"


class Conifer(Tree): #дочерний класс
    """
    Класс для хвойных деревьев, наследующий от Tree.

    Attributes:
        needle_length (float): Длина иголок в сантиметрах.
    """

    def __init__(self, species: str, height: float, age: int, needle_length: float) -> None:
        """
        Инициализация хвойного дерева.

        Args:
            species (str): Вид хвойного дерева.
            height (float): Высота хвойного дерева в метрах.
            age (int): Возраст хвойного дерева в годах.
            needle_length (float): Длина иголок в сантиметрах.
        """
        super().__init__(species, height, age)  # Вызов конструктора базового класса
        self._needle_length = needle_length  # Инкапсулированный атрибут для длины иголок

    def __str__(self) -> str:
        """
        Возвращает строковое представление хвойного дерева.

        Перегруженный метод для добавления информации о длине иголок,
        поскольку хвойные деревья имеют уникальную характеристику - длину иголок,
        которая важна для их описания.
        """
        return f"{super().__str__()} with needle length of {self._needle_length}cm"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление хвойного дерева.

        Перегруженный метод для включения информации о длине иголок,
        что позволяет более точно описать объект и его характеристики.
        """
        return f"Conifer(species='{self._species}', height={self._height}, age={self._age}, needle_length={self._needle_length})"

    def shed_needles(self) -> str:
        """
        Моделирует процесс сбрасывания иголок.

        Returns:
            str: Сообщение о сбрасывании иголок.

        Этот метод демонстрирует поведение хвойных деревьев и
        добавляет дополнительную функциональность, специфичную для этого класса.
        """
        return f"{self._species} is shedding its needles."

# Создание экземпляров деревьев
oak_tree = Tree("Oak", 15.0, 100)
spruce_tree = Conifer("Spruce", 20.0, 50, 2.5)

# Вывод информации о деревьях
print(oak_tree)
print(repr(oak_tree))

print(spruce_tree)
print(repr(spruce_tree))  

# Вызов метода сбрасывания иголок
print(spruce_tree.shed_needles())
