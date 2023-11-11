class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Privado

    def show(self):
        print(f"Nome: {self.name} - Salário: {self.salary}")
