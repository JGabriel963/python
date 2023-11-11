class Animal:
    name = ""
    size = ""
    color = ""

    def eat(self):
        print("Animal se alimentando")


class Horse(Animal):
    race = ""

    def escape(self):
        print("Cavalo fugindo")


class Lion(Animal):
    name = True

    def hunt(self):
        print("Leão caçando")


h = Horse()
h.name = "Pé de pano"
h.color = "Branco"
h.escape()
h.eat()

simba = Lion()
simba.name = "Simba"
simba.color = "marron"
simba.hunt()
simba.eat()
