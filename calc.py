def main ():
    soma = 0
    try:
        numeros = (input("Envie uma lista separada por virgula de numeros")).split(",")
        for num in numeros:
            soma = soma + int(num)
        print(f"Soma de {numeros} = {soma}")
    except ValueError:
        print("Input invalido")
        return

if __name__ == '__main__()':
    main()