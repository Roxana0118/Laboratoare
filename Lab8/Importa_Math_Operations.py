import Math_Operations

def main():
    a = float(input("Introduceți primul număr: "))
    b = float(input("Introduceți al doilea număr: "))

    print(f"Adunarea: {a} + {b} = {Math_Operations.adunare(a, b)}")
    print(f"Scăderea: {a} - {b} = {Math_Operations.scadere(a, b)}")
    print(f"Înmulțirea: {a} * {b} = {Math_Operations.inmultire(a, b)}")
    print(f"Împărțirea: {a} / {b} = {Math_Operations.impartire(a, b)}")

if __name__ == "__main__":
    main()