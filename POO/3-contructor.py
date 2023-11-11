class Movie:
    def __init__(self, name, year_launch, includePlan, note, duration):
        self.name = name
        self.year_launch = year_launch
        self.includePlan = includePlan
        self.note = note
        self.duration = duration

    def __str__(self):
        return f"Filme: {self.name} \nAno de Lançamento: {self.year_launch}"


mario = Movie("Super Mario Bros", "2023", False, 5.0, 130)
avatar = Movie("Avatar", "2023", False, 4.5, 220)
print(mario.name)
print(mario.note)
print(avatar)
