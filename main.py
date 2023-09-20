import random

#1
def zero():
    lst = []

    for i in range(100):
        lst.append(0)

    lst[0] = 1
    lst[-1] = 1

    print(lst)
    #print(len(lst))

#2
def up():
    lst = []

    for i in range(1, 51):
        if i % 2 == 0:
            lst.append(i)

    print(lst)

#3
def rnd():
    n = int(input('n: '))
    lst = []

    for i in range(10):
        lst.append(random.randint(0, 100))


    if n in lst:
        print(lst.index(n))
    else:
        print('-1')

#4
def summMult():
    lst = []

    for i in range(10):
        lst.append(random.randint(0, 100))

    summ = 0
    mult = 1

    for i in lst:
        summ += i
        mult *= i

    print(summ, '\n', mult)

#5
def maximum():
    lst = []

    for i in range(10):
        lst.append(random.randint(0, 100))

    print(max(lst))

#6
def repeat():
    lst = []

    for i in range(10):
        lst.append(random.randint(0, 100))

    print(lst)

    for i in lst:
        if lst.count(i) > 1:
            print(i)

#7
def change():
    lst = []

    for i in range(10):
        lst.append(random.randint(0, 100))

    lst2 = lst.copy()

    maximum = lst.index(max(lst))
    minimum = lst.index(min(lst))
    lst2[maximum] = min(lst)
    lst2[minimum] = max(lst)

    print(lst)
    print(lst2)

#8
def notEven():
    n = int(input('n: '))
    lst = []
    lst2 = []

    for i in range(n):
        number = int(input('number: '))
        lst.append(number)

    for i in range(len(lst)):
        if i % 2 != 0:
            lst2.append(i)
        
    lst2.reverse()

    for i in lst2:
        lst.pop(i)

    print(lst)

#9
def united():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    lst = []

    for i in a:
        if i in a and i in b:
            lst.append(i)

    print(lst)
