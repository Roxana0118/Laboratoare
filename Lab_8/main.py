from geometry import aria_cerc, circumferinta_cerc, aria_dreptunghi, perimetru_dreptunghi

def main():
    radius = float(input("Introduceți raza cercului: "))
    print(f"Aria cercului este: {aria_cerc(radius)}")
    print(f"Circumferința cercului este: {circumferinta_cerc(radius)}")

    length = float(input("Introduceți lungimea dreptunghiului: "))
    width = float(input("Introduceți lățimea dreptunghiului: "))
    print(f"Aria dreptunghiului este: {aria_dreptunghi(length, width)}")
    print(f"Perimetrul dreptunghiului este: {perimetru_dreptunghi(length, width)}")

if __name__ == "__main__":
    main()