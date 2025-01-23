def calculeaza_suma_fisier(nume_fisier):
    try:
        suma = 0
        with open(nume_fisier, 'r') as fisier:
            for linie in fisier:
                try:
                    numar = float(linie.strip())  # Convertim linia la număr
                    suma += numar
                except ValueError:
                    print(f"Valoare invalidă pe linie: {linie.strip()}")
        return suma
    except FileNotFoundError:
        return "Eroare: Fisierul nu a fost găsit!"
    except IOError:
        return "Eroare: A apărut o problemă la citirea fișierului!"

nume_fisier = "numere.txt"  # Înlocuiește cu calea reală a fișierului
rezultat = calculeaza_suma_fisier(nume_fisier)
print(rezultat)
