class Inventar:
    def __init__(self):
        self.produse = {}  # Dicționar pentru stocarea produselor (nume_produs: cantitate)

    def adauga_produs(self, nume, cantitate):
        try:
            cantitate = int(cantitate)
            if cantitate < 0:
                raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
            if nume in self.produse:
                self.produse[nume] += cantitate
            else:
                self.produse[nume] = cantitate
            print(f"Produsul '{nume}' a fost adăugat cu succes!")
        except ValueError as e:
            print(f"Eroare: {e}")

    def cauta_produs(self, nume):
        try:
            if nume in self.produse:
                print(f"Produs: {nume}, Cantitate: {self.produse[nume]}")
            else:
                raise KeyError(f"Produsul '{nume}' nu există în inventar.")
        except KeyError as e:
            print(e)

    def actualizeaza_cantitate(self, nume, cantitate):
        try:
            cantitate = int(cantitate)
            if nume not in self.produse:
                raise KeyError(f"Produsul '{nume}' nu există în inventar.")
            if cantitate < 0:
                raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
            self.produse[nume] = cantitate
            print(f"Produsul '{nume}' a fost actualizat cu succes! Cantitate nouă: {cantitate}")
        except (KeyError, ValueError) as e:
            print(f"Eroare: {e}")

    def afiseaza_inventar(self):
        if not self.produse:
            print("Inventarul este gol.")
        else:
            print("Inventar:")
            for nume, cantitate in self.produse.items():
                print(f"- {nume}: {cantitate}")


# Program principal
def meniu():
    inventar = Inventar()
    while True:
        print("\nMeniu:")
        print("1. Adaugă produs")
        print("2. Caută produs")
        print("3. Actualizează cantitatea unui produs")
        print("4. Afișează inventarul")
        print("5. Ieșire")

        optiune = input("Alege o opțiune: ")
        if optiune == "1":
            nume = input("Introdu numele produsului: ")
            cantitate = input("Introdu cantitatea: ")
            inventar.adauga_produs(nume, cantitate)
        elif optiune == "2":
            nume = input("Introdu numele produsului: ")
            inventar.cauta_produs(nume)
        elif optiune == "3":
            nume = input("Introdu numele produsului: ")
            cantitate = input("Introdu noua cantitate: ")
            inventar.actualizeaza_cantitate(nume, cantitate)
        elif optiune == "4":
            inventar.afiseaza_inventar()
        elif optiune == "5":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă. Te rog să încerci din nou.")

# Pornim programul
meniu()
