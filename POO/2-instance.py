class Movie:
    name = ""
    year_launch = 0
    includePlan = False
    note = 0
    duration = 0


# Primeiro Filme
movie = Movie()
movie.name = "Super Mario Bros"
movie.year_launch = 2023
movie.includePlan = False
movie.note = 5.0
movie.duration = 130
print("##Dados do Filme##")
print(f"Nome do filme: {movie.name} \nAno de Lançamento: {movie.year_launch}")
