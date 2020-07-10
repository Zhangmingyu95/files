__author__ = 'mingyu.zhang'
class Animal():
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):

    def run(self):
        print('Cat is running...')
class people(object):
    def run(self):
        print("people do not extends Animal")
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Cat())
run_twice(Animal())
run_twice(people())