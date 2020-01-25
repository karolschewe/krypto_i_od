from main import phi
from odwrotnosc import odwrotnosc_modulo
'''
program przedstawia przykladowe dzialanie RSA
'''

#po pierwsze wybieramy dwie liczby pierwsze p i q oraz klucz publiczny e, ustalmy tez wiadomosc do wyslania m
p = 7
q = 13
e = 5
m = 2
# n = pq -- wazne jest aby n bylo liczba bezkwadratowa -- nie dzielila sie przez kwadrat liczby pierwszej dla pewnosci spojrzec chociaz
# czy nie jest podzielna przez 4 i 9 i 25
n = p * q
print(f'n = pq: {n}')

# nastepnie wyznaczamy wartosc fi(n)
fi_n = phi(n)
print(f'phi(n):{fi_n}')

#klucz prywatny jest odwrotnoscia klucza prywatnego w mod fi_n
d = odwrotnosc_modulo(e,fi_n)
print(f'klucz prywatny d: {d}')

# wyliczmy kryptogram c
c = (m ** e) % n
print(f'kryptogram c: {c}')

# aby odtworzyc spowrotem wiadomosc nalezy:

expected_m =( c ** d ) % n

print(f'odtworzona wiadomosc z kryptogramu: {expected_m}')