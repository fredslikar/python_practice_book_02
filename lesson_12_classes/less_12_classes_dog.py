class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight >= 20:
            print(self.name,'make "VUF-VUF!')
        if self.weight < 20:
            print(self.name, 'make "vuf-vuf!')

    def human_age(self):
        h_a = self.age * 7
        print('Human age of dog', self.name, 'is', h_a, 'year(s)!')

    def __str__(self):
        return "I'm dog and my name is " + self.name

def print_dog(dog):
    print(dog.name, ': age is -', dog.age, 'year(s) - weight is -', dog.weight, 'kg')


class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        self.isworking = False

    def bark(self):
        if self.isworking:
            print('I can"t barking, i"m working!')
        else:
            Dog.bark(self)

    def sdog_work(self):
        print(self.name, 'helps for', self.handler, 'walk!')


class FrisbeeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

    def bark(self):
        if self.frisbee != None:
            print("I can't barking, be couse i'm holding the " + self.frisbee.color + " frisbee!")
        else:
            Dog.bark(self)

    def catch(self, frisbee):
        self.frisbee = frisbee
        print(self.name, "cath the", frisbee.color, 'frisbee!')

    def give(self):
        if self.frisbee != None:
            frisbee = self.frisbee
            self.frisbee = None
            print(self.name, 'gave', frisbee.color, 'frisbeedisk!')
            return frisbee
        else:
            print(self.name, "don't have any frisbee...")
            return None

    def __str__(self):
        if self.frisbee != None:
            return Dog.__str__(self) + ' and i have the ' + self.frisbee.color + ' frisbee)))'
        else:
            return Dog.__str__(self)


class Frisbee:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'Hi, i"m ' + self.color + ' frisbee!'


tuzik = Dog('Tuzik', 3, 10)
jekson = Dog('Jekson', 5, 20)
rody = ServiceDog('Rody', 5, 25, 'Stive')

def test_code():

    jim = FrisbeeDog('Jim', 7, 15)
    disk1 = Frisbee('blue')
    disk2 = Frisbee('red')

    print(jim)
    jim.bark()
    jim.catch(disk1)
    jim.bark()
    print(jim)
    frisbee = jim.give()
    print(frisbee)
    print(jim)
    jim.give()

test_code()