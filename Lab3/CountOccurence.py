def numara_cuvinte (propozitie):
    propozitie = propozitie.lower()
    cuvinte = propozitie.split()
    frecventa = {}

    for cuvant in cuvinte:
        if cuvant in frecventa:
            frecventa[cuvant] += 1
        else:
            frecventa[cuvant] = 1
    return frecventa
propozitie = input("Introduceti propozitia: ")
rezultat = numara_cuvinte(propozitie)
print("Frecventa este:")
for cuvant, aparitii in rezultat.items():
    print(f"{cuvant} : {aparitii}")