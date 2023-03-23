from datetime import date
current_year = date.today().year
year = int(input("Ano de nascimento: "))
age = current_year - year
print(f'Quem nasceu em {year} tem {age} anos em {current_year}')
if age == 18:
    print("Alistamento IMEDIATAMENTE!")
elif age < 18:
    print(f'Ainda faltam {18 - age} para o alistamento.')
    print(f'Seu alistamento será em {current_year + (18 - age)}.')
elif age > 18:
    print(f'Você já deveria ter se alistado há {age - 18} anos.')
    print(f'Sue alistamento foi em {current_year - (age - 18)} anos.')


