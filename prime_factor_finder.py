# This program finds the largest prime factors of a number



number = input("What number would you like to find the prime factors of? (+ve integers only): ")

number = int(number)

factorlist = []

multiplier = number

a = 2

while a < multiplier + 1:
    if multiplier % a ==0:
        multiplier = multiplier / a
        factorlist.append(a)
        if multiplier == 1:
            break
        a = 2
    else:
        a = a + 1

print ("The prime factors of ", number, "are", factorlist)


