# Função para retornar a string com a forma correta para os números
def plural(n, singular, plural):
    return singular if n == 1 else plural

# Função para converter dígitos em palavras
def converter_para_palavras(n):
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

    if n < 10:
        return unidades[n]
    elif n < 20:
        return especiais[n - 10]
    else:
        return dezenas[n // 10] + (" e " + unidades[n % 10] if n % 10 != 0 else "")

# Leitura do número do usuário
num = int(input('Digite um número inteiro menor que 1000: '))

# Validação do número
if num >= 1000:
    print("O número deve ser menor que 1000.")
else:
    # Separação de centenas, dezenas e unidades
    centenas = num // 100
    dezenas = (num % 100) // 10
    unidades = num % 10

    # Conversão para palavras
    resultado = ""
    if centenas > 0:
        resultado += converter_para_palavras(centenas) + " " + plural(centenas, "centena", "centenas")
    if dezenas > 0:
        if centenas > 0:
            resultado += ", "
        resultado += converter_para_palavras(dezenas * 10 + unidades)
    elif unidades > 0:
        if centenas > 0:
            resultado += " e "
        resultado += converter_para_palavras(unidades)

    # Impressão do resultado
    resultado += plural(num, " número", " números")
    print(resultado + ".")
