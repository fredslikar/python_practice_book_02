def drink(param):
    msg = "drink " + param + " glas!"
    print(msg)
    param = "empty"


volume = "full"
drink(volume)
print("Glas", volume)

greeting = "Hello!"


def greet(name, massage):
    global greeting
    greeting = "Hi!"
    print(name + greeting + massage)


greet("Ivan ", " See you!")
print(greeting)
