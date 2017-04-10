

def prime1(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime(n):
    for p in range(2, n+1):
        if prime1(p):
            print p


def factorial(n):
    p = 1
    for i in range(1, n+1):
       p = p * i
    return p

def combination(n, r):
    return factorial(n)/(factorial(r) * factorial(n - r))

def quitcont(n):
    if n == "E" or n == "e":
        quit()
    else:
        return menu()
def menu():
    menum = raw_input("Please press P for Prime Numbers: \nPlease press C for Combination: \n")
    if menum == "C" or menum == "c":
        value = input("Please enter value of n: \n")
        value2 = input("Please enter value of r: \n")
        print combination(value, value2)
    elif menum == "P" or menum == "p":
        val = input("Please enter value for find prime numbers till value: \n")
        prime(val)
    qcont = raw_input("Please Press Enter for New Calculation: \nPlease press E for exit: \n")
    quitcont(qcont)

menu()
