# jak uzywac tego programu
# jezeli mamy kongruencje 1 mod (6) nalezy uzupelnic a = 1 a_mod 7
# jezeli mamy uklad kodgruencji ( do 4 kongruencji ) uzupelniamy wedlug wzoru
# jak mamy uklad np 3 kongruencji to w d d_mod przypisujemy None
a = 5
a_mod = 7
b = 3
b_mod = 5
c = 11
c_mod = 13
d = 9
d_mod = 11

print(f'pierwsza kongruencja: {a} mod {a_mod}')
number = 0
while number % a_mod != a:
    number += 1
print(f'druga kongruencja: {b} mod {b_mod}')
while number % b_mod != b:
    number+=a_mod
    print(number)
print(f"trzecia kongruencja {number} mod {a_mod*b_mod}")
while number % c_mod != c:
    number += a_mod*b_mod
    print(number)
print(f'trzecia kongruencja: {number} mod {a_mod*b_mod*c_mod}')
while number % d_mod != d:
    number += a_mod * b_mod * c_mod
    print(number)
print(f'ostateczny wynik: {number} mod {a_mod * b_mod * c_mod * d_mod}')


















