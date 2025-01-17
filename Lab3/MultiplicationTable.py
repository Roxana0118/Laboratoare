#multiplication table generator
number = int(input("Intorduceti un numar: "))
table_limit = int(input("Introduceti de cate ori sa fie multiplicat: "))

if table_limit <= 0:
    print("Numarul trebuie sa fie un numar pozitiv.")

print(f"\n Tabelul de inmultire pentru {number}:")

for i in range(1, table_limit + 1):
        print(f"{number} x {i} = {number * i}")
