number = int(input("Introduceti un numar: "))
factorial = 1

if number < 0:
    print("Numar negativ. Nu exista factorial.")
if number == 0:
    print("Factorialul numarului 0 este 1.")
else:
    for i in range(1, number+1):
        factorial=factorial*i
    print("Factorialul lui",number,"este",factorial)