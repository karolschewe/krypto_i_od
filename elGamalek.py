# programik odtwarza system podpisow cyfrowych elgamala
import odwrotnosc

#parametry poczatkowe:
p = 13 #dowolna liczba pierwsza
g = 2 # dowolny generator grupy multiplikatywnej p (mozna wyznaczyc w programie main.py)
x = 3 # tajny klucz prywatny -- dowolny z przedziału <2, p-2>
m = 4 # wiadomość -- dowolna z przedziału <0, p-2>
k = 5 # potrzebujemy liczby k, ktora jest kopierwsza z p-1 -- czyli gcd(k,p-1) = 1 -- patrz main.py
#parametry^^^


from main import gcd
if gcd(k,p-1) > 1:
    print(f'k: {k} nie jest liczba kopierwsza z {p-1}')
    raise Exception

y = (g**x)%p #klucz publiczny
print(f'klucz publiczny: {y}')
# podpis jest para liczb a i b

# liczymy liczbe odwrotna do k w pierscieniu p-1
k_odwrotnosc = odwrotnosc.odwrotnosc_modulo(k,p-1)

# w koncu wyznaczmy a
a = (g**k) % p
#oraz b
b = (k_odwrotnosc * (m - (x * (a % (p-1))) % (p-1)) % (p-1)) % (p-1)
print(f'a: {a}')
print(f'b: {b}')


#### sprawdzenie czy sie zgadza podpis#######
L = ((y**a) * (a**b)) % p
P =(g**m) % p
if L == P:
    print(f"uzyskano autentykację L:{L} = P:{P}")