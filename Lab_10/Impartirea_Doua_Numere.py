def imparte(numar1, numar2):
    try:
        rezultat = numar1 / numar2
        return rezultat
    except ZeroDivisionError:
        return "Eroare: Împărțire la zero nu este permisă!"

# Exemplu de utilizare
print(imparte(10, 2))  # Va returna 5.0
print(imparte(10, 0))  # Va returna "Eroare: Împărțire la zero nu este permisă!"