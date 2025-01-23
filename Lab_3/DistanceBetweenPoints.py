import math

def distanta(x1, y1, x2, y2):
    return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)

x1 = int(input("Introduceti prima coordonata primului punct: "))
y1 = int(input("Introduceti a doua coordonata primului punct: "))
x2 = int(input("Introduceti prima coordonata pentru al doilea  punct: "))
y2 = int(input("Introduceti a doua coordonata pentru al doilea punct: "))

dist = distanta(x1,y1,x2,y2)

print(f"Distanta dintre puntele ({x1},{y1}) si ({x2},{y2}) este : {dist}")