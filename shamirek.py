
'''
Prawdopodobienstwo oszustwa przy uwierzytelnieniu z fiata-shamira wynosi 2^-kt
gdzie: t jest liczbą powtórzeń algorytmu
a k jest dlugoscia sekretu
'''



'''
algorytm dzielenia tajemicy shamira polega na wybraniu liczby n osob do podzialu
nastepnie wybieramy liczbe pierwsza p
potem ustalamy prog t
na koncu wybieramy wielomian stopnia < t tak aby wartosc naszego sekretu byla wartoscia wielomianu w punkcie x (efektywnie c = sekret)
wybieramy n punktow na wielomianie ktore bedziemy wyznaczac
nastepnie wyznaczamy wartosci wielomianu w tych punktach w modulo p
osoby znaja jedynie wartosci modulo tych punktow
jezeli mamy wystarczajaca liczbe punktow mozna wyznaczyc rozwiazanie ze wzoru interpolacyjnego lagrange'a
'''

# przykladowe rozwiazanie interpolujace
# a(1) = 3
# a(2) = 15
# a(3) = 4
x = [1,2,3]
y = [3,15,4]
modulko = 19
sumka = 0
for i in x:
    print(i.__index__())
    iloczynek = y[i.__index__()-1]
    for j in x:
        if i != j:
            iloczynek = iloczynek * ( j/ (j-i) )
    sumka += iloczynek

print(f'tajemnica: {sumka%modulko}')