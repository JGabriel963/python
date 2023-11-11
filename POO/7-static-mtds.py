class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail

    @staticmethod
    def course_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominando Python", "Módulos e Pip", "Orientação a Objetos"]
        elif trail == "Automação com Python":
            courses = [
                "Automoção de Tarefas",
                "Web Scraping",
                "Assistente Virtual em Python",
            ]
        else:
            courses = ["A definir"]
        return courses


print(Course.course_trail("Python Fundamentos"))
print(Course.course_trail("Análises de Dados"))
print(Course.course_trail("Automação com o Python"))
