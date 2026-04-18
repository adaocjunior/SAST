import os
import sqlite3

def main():
    try:
        # Input separado por contexto
        numeros = input("Envie uma lista separada por virgula de numeros: ")
        usuario = input("Digite seu nome de usuário: ")

        # Processamento normal
        lista = numeros.split(",")
        soma = 0

        for num in lista:
            soma += int(num)

        print(f"Soma = {soma}")

        #Vulnerabilidade 1: SQL Injection (CWE-89)
        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, total INTEGER)")

        query = f"INSERT INTO users (username, total) VALUES ('{usuario}', {soma})"
        cursor.execute(query)

        conn.commit()
        conn.close()

        # Vulnerabilidade 2: Command Injection (CWE-78)
        os.system(f"echo Usuario {usuario} calculou soma {soma} >> log.txt")

    except ValueError:
        print("Input invalido")

if __name__ == '__main__':
    main()