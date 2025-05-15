def main():

    for i in range(10):
        print("*", end=" ")
    print()
    for i in range(5):
        print("*", end=" ")
    print()
    for i in range(20):
        print("*", end=" ")

def second():
    for i in range(10):
        for j in range(10):
            print("*", end=" ")
        print()

def third():
    for i in range(10):
        for j in range(5):
            print("*", end=" ")
        print()

def fourth():
    for i in range(5):
        for j in range(20):
            print("*", end=" ")
        print()

def fifth():
    for i in range(10):
        for j in range(10):
            print(j, end=" ")
        print()

def sixth():
    for i in range(10):
        for j in range(10):
            print(i, end=" ")
        print()

def seventh():
    for i in range(10):
        for j in range(i + 1):
            print(j, end=" ")
        print()

def eighth():
    for i in range(10):
        for j in range(i):
            print(" ", end=" ")
        for j in range(10 - i):
            print(j, end=" ")
        print()

def ninth():
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j < 10:
                print(" ", end="")
            print(i * j, end=" ")
        print()

def tenth():
    for i in range(10):
        for j in range(10 - i):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()

third()