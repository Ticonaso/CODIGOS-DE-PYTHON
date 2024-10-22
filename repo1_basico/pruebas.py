lista = [5,7,2,7,9,4,8]

print (lista[6])

lista.sort()

print(lista[-2])

#2

def conversor(d,h,m,s):

    final = 0
    h = d * 24
    m = h * 60
    s = m * 60
    final = s * 1000
    return final

x = conversor(2,0,0,0)
print(x)

#3

def fizzbuzz():
    for a in range(1,101):
        if a % 3 == 0 and a % 5 == 0:
            print("fizzbuzz")
        elif a % 3 == 0:
            print("fizz")
        elif a % 5 == 0:
            print("buzz")
        else:
            print(a)

fizzbuzz()