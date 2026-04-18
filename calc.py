import sqlite3
import re

def main():
    try:
        numeros = input("Envie uma lista separada por virgula de numeros: ")
        usuario = input("Digite seu nome de usuário: ")

        # Validar username
        if not re.match(r'^[a-zA-Z0-9_]+$', usuario):
            raise ValueError("Username inválido")


        lista = numeros.split(",")
        soma = 0

        for num in lista:
            num = num.strip()
            if not num.isdigit():
                raise ValueError("Apenas números são permitidos")
            soma += int(num)

        print(f"Soma = {soma}")

        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, total INTEGER)")

        cursor.execute(
            "INSERT INTO users (username, total) VALUES (?, ?)",
            (usuario, soma)
        )

        conn.commit()
        conn.close()

        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"Usuario {usuario} calculou soma {soma}\n")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()