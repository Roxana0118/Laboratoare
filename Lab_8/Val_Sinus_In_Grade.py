import math

# Date de intrare
angle = float(input("Introduceți un unghi în grade pentru a calcula sinusul: "))

# Conversia unghiului din grade în radiani
angle_rad = math.radians(angle)

# Calcularea valorii sinusului
sin_angle = math.sin(angle_rad)

# Afișarea rezultatului
print(f"Sinusul unghiului de {angle} grade este {sin_angle}")