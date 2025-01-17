numar=int(input("Introduceti un numar: "))
if numar > 1:
    for i in range(2, numar):
        if numar % i == 0:
            print(f"{numar} nu este un numar prim.")
            break
        else:
            print(f"{numar} este un numar prim.")
else:
    print(f"{numar} nu este un numar prim.")