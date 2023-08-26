# Создать класс Person, который содержит: 

# переменные fullName, age - должны быть закрыты;
# методы move() и talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит". 
# создайте геттеры и сеттеры для закрытых полей класса
# Создайте два объекта этого класса. 
# Вызовите методы move() и talk().


class Person:
    def __init__(self, fullName, age):
        self.__fullName = fullName
        self.__age = age

    # Геттеры
    def get_full_name(self):
        return self.__fullName

    def set_full_name(self, name):
        self.__fullName = name
        
    # Сеттеры    
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        
    
    def move(self, message):
        print(f'{self.__fullName} идет - {message}')

    def talk(self, message):
        print(f'{self.__fullName} говорит - {message}')

# Создание объектов
dude1 = Person('Chack', 23)
dude2 = Person('Korvo', 19)

# Вызов методов
dude1.move('в магаз за пивом')
dude2.move('рядом с Chack\n')

dude1.talk('боюсь однажды меня заменят...')
dude2.talk('не переживай, этого не случится!\n')


#Применение Сеттера и Геттера
dude1.set_full_name('Jack')
print(f'Chack заменен на {dude1.get_full_name()}' )

dude1.set_age(25)
print(f'Возраст был 23, а стал {dude1.get_age()}\n'
      f'Korvo остался собой')
        
        
# Вывод консоли
# Chack идет - в магаз за пивом
# Korvo идет - рядом с Chack

# Chack говорит - боюсь однажды меня заменят...
# Korvo говорит - не переживай, этого не случится!

# Chack заменен на Jack
# Возраст был 23, а стал 25
# Korvo остался собой