
def odwrotnosc_modulo(liczba: int, modulo: int):
    for i in range(modulo):
        if liczba*i % modulo == 1:
            return i
    return None

