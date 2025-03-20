
print("A Monster is attacking you!")
print()
class Cat:
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = 0

    def meow(self):
        var = input("Do you attack the Monster? (Y/N): ")
        if var.upper() == "Y":
            var2 = input("Do you use a strong or a weak attack? ")
            if var2.lower() == "strong" or var2.lower() == "strong attack":
                print()
                print("Meow!")
                monster.decrease_health(100)
            elif var2.lower() == "weak" or var2.lower() == "weak attack":
                print()
                print("Meow...!")
                monster.decrease_health(50)
        elif var.upper() == "N":
            print()
            print("Meow.")
            print("The Monster walks away.")

def main():
    cat = Cat()
    cat.name = "Nelly"
    cat.color = "Grey"
    cat.weight = 3
    cat.meow()

class Monster:
    def __init__(self):
        self.name: str = ""
        self.health: int = 0


    def decrease_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("The " + self.name + " is dead.")
            exit()



monster = Monster()
monster.name = "monster"
monster.health = 100
monster.decrease_health(0)
while monster.health > 0:
    main()
    print("The " + monster.name + " is not dead yet.")


main()