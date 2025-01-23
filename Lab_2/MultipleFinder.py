numar = int(input("Introduceti un numar: "))
start = int(input("Introduceti valoarea de start: "))
sfarsit = int(input("Introduceti valoarea de sfarsit : "))
multiplii=[] # stocam toti multiplii gasiti
for i in range(start, sfarsit+1):
    if i%numar==0:
        multiplii.append(i) #adauga elementul i(un multiplu al numarului) se adauga la lista multiplii
if multiplii:
    print(f"Multiplii lui {numar} între {start} și {sfarsit} sunt: {multiplii}")
else:
    print(f"Nu există multiplii ai lui {numar} în intervalul {start} până la {sfarsit}.")