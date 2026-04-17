def main ():
    soma = 0
    try:
        numeros = eval(input("Envie uma lista separada por virgula de numeros"))
    except SyntaxError:
        print("Input invalido")
    for num in numeros:
        soma = soma + num
    print(f"Soma de {numeros} = {soma}")

if __name__ == '__main__()':
    main()