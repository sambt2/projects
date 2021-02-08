# This program finds all primes up to a specified number. 

list_of_primes = [2]
length = 1

print ("This programme finds prime numbers up to a specified number.")
cap = int(input("Which number would you like to go up to? "))


for n in range (3, 99999999999):
    if n > cap - 1:
        break
    
    else:
        result = 1
        for t in range (0, length):
            if n/list_of_primes[t] == int(n/list_of_primes[t]):
                result = 0
                break
        if result == 1:
            list_of_primes.append(n)
            print ("Adding ", n, " to the list of primes")
            length = length + 1

print ("The list of primes up to ", cap, "is ", list_of_primes)

                                 
