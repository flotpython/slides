import primesieve
import time
def prime_stat(top):
    n=0
    primes = primesieve.Iterator()
    beg=time.time()
    while True:
        if primes.next_prime() >= top:
            break
        n += 1
    end=time.time()
    print(f"{end-beg:.2f}s to enumerate {n} primes lower than {top} (ratio = {100*n/top} %)")

for power in range(2, 11):
     prime_stat(10**power)
