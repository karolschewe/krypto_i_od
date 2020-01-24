# A simple Python3 program
# to calculate Euler's
# Totient Function

# Function to return
# najwiekszy wspolny dzielnik
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)



# A simple method to evaluate
# Euler Totient Function
def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result

#print(phi(5**10))

def getGenerators(n):
    generators = []
    for ints in range(2,n+1):
        outcomes = []
        for powers in range (1, n):
            powerResult = ints**powers
            moduloRes = powerResult%n
            if moduloRes in outcomes:
                break
            else:
                outcomes.append(moduloRes)
            if powers == n - 1:
                generators.append(ints)
    return generators
if __name__ == '__main__':
    print("generatory wielokrotnosci 4 i 6 i 9 i 10 i 14")
    print(getGenerators(4 * 6 * 9 * 10 * 14))
    # wielokrotnosci 4 i 6 i 9 i 10 i 14nie maja generatorow
    # grupa n powinna miec phi(phi(n)) generatorow
    print(getGenerators(5))
    print("liczba generatorow 5:")

    print(phi(phi(5)))
    print(getGenerators(17))
    print("liczba generatorow 17:")
    print(phi(phi(17)))

    print(phi(5))
    print(phi(phi(13)))
    print(getGenerators(19))

    print(phi(5358))
    print(phi(1656))
    print(phi(3458))
    print(phi(1296))
