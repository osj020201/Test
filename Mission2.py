name = str(input("이름을 입력하세요.: "))
gender = str(input("성별을 입력하세요.(male or female): "))
age = int(input("나이를 입력하세요.: "))



class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print('이름: %s' % (self.name), '성별: %s' % (self.gender))
        print('나이: %d' % (self.age))

person = Person(name, gender, age)
person.display()