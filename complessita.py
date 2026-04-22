def esempio_lineare(lista):
    # Questo algoritmo ha complessità O(n)
    for elemento in lista:
        print(f"Elaborazione: {elemento}")

if __name__ == "__main__":
    dati = [10, 20, 30, 40, 50]
    esempio_lineare(dati)