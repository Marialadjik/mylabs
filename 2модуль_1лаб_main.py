import self as self
#первый класс
import doctest
class SocialMedia:
    """
    Документация на класс.
    Класс описывает модель профиля социальной сети.
    """
    def __init__(self, name: str, nickname: str):
        """Инициализация экземпляра класса."""
        self.name = "Вася Васечкин" #Имя и фамилия пользователя
        self.nickname = "Vasiliy_Vasechkin2004" #Никнейм пользователя
        self.posts = []  # Список для хранения публикаций

    def add_post(self, content: str):
        """ Добавляет новый пост в профиль. """
        post = {
            'content': content,
            'likes': 0,
            'comments': []
        }
        self.posts.append(post)

    def like_post(self, post_index: int):
        """ Увеличивает количество лайков у поста. """
        if 0 <= post_index < len(self.posts):
            self.posts[post_index]['likes'] += 1
        else:
            print("Пост с таким индексом не существует.")

    def display_profile(self):
        """Отображает информацию о профиле."""
        print(f"Имя: {self.name}")
        print(f"Никнейм: {self.nickname}")
        print(f"Публикации: {len(self.posts)}")
        for index, post in enumerate(self.posts):
            print(f"  Пост {index + 1}: {post['content']} (Лайков: {post['likes']})")

#Пример использования
if __name__ == "__main__":
    profile = SocialMedia("Вася Васечкин", "Vasiliy_Vasechkin2004")
    profile.add_post("Привет, мир!")
    profile.like_post(0)
    profile.display_profile()

    doctest.testmod()  # тестирование примеров, которые находятся в документации
    help(SocialMedia)








#второй класс
import doctest

class Garden:
    """
    Документация на класс.
    Класс описывает модель итогового числа фруктов в саду.
    """
    def __init__(self, apples: int, bananas: int):
        """ Инициализация экземпляра класса. Ожидаемое количество урожая"""
        self.apples = 30
        self.bananas = 15

    def add_apples(self, count: int):
        """ Добавляет указанное количество яблок.

        >>> garden = Garden(10, 5)
        >>> garden.add_apples(5)
        >>> garden.apples
        15
        """
        self.apples += count

    def add_bananas(self, count: int):
        """ Добавляет указанное количество бананов.

        >>> garden = Garden(10, 5)
        >>> garden.add_bananas(3)
        >>> garden.bananas
        8
        """
        self.bananas += count

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    help(Garden)










#третий класс
import doctest
class Students:
    """
    Документация на класс.
    Класс описывает модель информации о студенте.
    """
    def __init__(self, name: str, age: int):
        """ Инициализация экземпляра класса. """
        self.name = name
        self.age = age

    def get_info(self):
        """ Возвращает информацию о студенте.
        >>> student = Students("Алёна Кузнецова", 20)
        >>> student.get_info()
        'Имя: Алёна Кузнецова, Возраст: 20'
        """
        return f'Имя: {self.name}, Возраст: {self.age}'

    def set_name(self, name: str):
        """ Устанавливает имя студента.
        >>> student = Students("Алёна Кузнецова", 20)
        >>> student.set_name("Иван Иванов")
        >>> student.get_info()
        'Имя: Иван Иванов, Возраст: 20'
        """
        self.name = name

    def set_age(self, age: int):
        """ Устанавливает возраст студента.
        >>> student = Students("Алёна Кузнецова", 20)
        >>> student.set_age(21)
        >>> student.get_info()
        'Имя: Алёна Кузнецова, Возраст: 21'
        """
        self.age = age

if __name__ == "__main__":
    # Пример использования класса Students
    student1 = Students("Алёна Кузнецова", 20)
    print(student1.get_info())  # Вывод информации о студенте

    # Изменение имени студента
    student1.set_name("Иван Иванов")
    print(student1.get_info())  # Вывод новой информации о студенте

    # Изменение возраста студента
    student1.set_age(21)
    print(student1.get_info())  # Вывод обновленной информации о студенте

    doctest.testmod()  # тестирование примеров, которые находятся в документации
    help(Students)