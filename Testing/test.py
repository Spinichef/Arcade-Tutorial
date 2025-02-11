def test():

    user_name = (input("What is your name? "))
    if user_name.lower() == "jonas":
        print("You have a good name!")
    elif user_name.lower() == "bene" or user_name.lower() == "benedikt":
        print("You have a bad name!")
    elif user_name.lower() == "fickdich" or user_name.lower() == "fick dich":
        for i in range(5):
            print("Bene sei leise.")
    else:
        print("You have an ok name!")

def test2():
    for i in range(10):
        for j in range(10):
            print("Bene sei leise.")
test2()