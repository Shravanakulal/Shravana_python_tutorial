class person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print('talk')

john = person('John Smith')
print(john.name)
john.talk()