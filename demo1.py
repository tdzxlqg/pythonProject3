class Animal:
    def __init__(self):
        print('Animal init')
class Bird(Animal):
    def __init__(self, hungry):
        super().__init__()
        self.hungry = hungry
    def eat(self):
        if self.hungry:
            print('已经吃了虫子了，不饿了！')
            self.hungry = False
        else:
            print("已经吃过饭了，不饿了！")
b = Bird(True)
b.eat()
b.eat()
