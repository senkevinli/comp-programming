import sys
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

numPrimes = 0 

i = 0 

while(i < len(primes)): 
    guess = primes[i] 
    print("? " + str(guess))
    stdout.flush() 
    string = input()
    if string == "yes": 
        if primes[i] < 10: 
            primes[i] = primes[i] * primes[i]   
        numPrimes += 1 
        if numPrimes == 2: 
            print("! composite")
            stdout.flush()
            break
    else: 
        i += 1
if numPrimes < 2: 
    print("! prime")
    stdout.flush()