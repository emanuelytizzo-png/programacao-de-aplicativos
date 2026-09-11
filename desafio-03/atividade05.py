import random
import time
import sqlite3

numeros = [random.randint(1, 10000) for _ in range(1000)]

lista_python = numeros.copy()

inicio_python = time.perf_counter()

for i in range(len(lista_python)):
    for j in range(0, len(lista_python) - i - 1):

        if lista_python[j] > lista_python[j + 1]:
            lista_python[j], lista_python[j + 1] = (
                lista_python[j + 1],
                lista_python[j]
            )

fim_python = time.perf_counter()

tempo_python = fim_python - inicio_python

conn = sqlite3.connect("benchmark.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS numeros")

cursor.execute("""
    CREATE TABLE numeros (
        numero INTEGER
    )
""")

cursor.executemany(
    "INSERT INTO numeros (numero) VALUES (?)",
    [(numero,) for numero in numeros]
)

conn.commit()


inicio_sqlite = time.perf_counter()

cursor.execute("""
    SELECT numero
    FROM numeros
    ORDER BY numero ASC
""")

resultado = cursor.fetchall()

fim_sqlite = time.perf_counter()

tempo_sqlite = fim_sqlite - inicio_sqlite
print(f"Tempo Bubble Sort: {tempo_python:.6f} segundos")
print(f"Tempo SQLite ORDER BY: {tempo_sqlite:.6f} segundos")

if tempo_python < tempo_sqlite:
    print("O Bubble Sort foi mais rápido neste teste.")
elif tempo_sqlite < tempo_python:
    print("O SQLite ORDER BY foi mais rápido neste teste.")
else:
    print("Os dois métodos tiveram o mesmo tempo.")

conn.close()
