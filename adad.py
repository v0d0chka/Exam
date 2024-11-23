class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class Person:
    def __init__(self, name):
        self.name = name
        self.age = None

    def set_age(self, age):
        if age < 0 or age > 120:
            raise InvalidAgeError(f" {age} can not be ?  only 0 - 120")
        self.age = age

    def __str__(self):
        return f"Персонаж {self.name}, возраст: {self.age}"

def test_person():
    person = Person("Иван")

    try:
        person.set_age(25)
        print(person)

        person.set_age(-5)
    except InvalidAgeError as e:
        print(f"Ошибка: {e.message}")

    try:
        person.set_age(130)
    except InvalidAgeError as e:
        print(f"Ошибка: {e.message}")

test_person()