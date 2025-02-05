"""The numbers 12, 63 and 119 have something in common related with their divisors and their prime factors, let's see it.

Numbers PrimeFactorsSum(pfs)        DivisorsSum(ds)              Is ds divisible by pfs
12         2 + 2 + 3 = 7         1 + 2 + 3 + 4 + 6 + 12 = 28            28 / 7 = 4,  Yes
63         3 + 3 + 7 = 13        1 + 3 + 7 + 9 + 21 + 63 = 104         104 / 13 = 8, Yes
119        7 + 17 = 24           1 + 7 + 17 + 119 = 144                144 / 24 = 6, Yes
There is an obvius property you can see: the sum of the divisors of a number is divisible by the sum of its prime factors.

We need the function ds_multof_pfs() that receives two arguments: nMin and nMax, as a lower and upper limit (inclusives), respectively, and outputs a sorted list with the numbers that fulfill the property described above.

We represent the features of the described function:

ds_multof_pfs(nMin, nMax) -----> [n1, n2, ....., nl] # nMin ≤ n1 < n2 < ..< nl ≤ nMax
Let's see some cases:

ds_multof_pfs(10, 100) == [12, 15, 35, 42, 60, 63, 66, 68, 84, 90, 95]

ds_multof_pfs(20, 120) == [35, 42, 60, 63, 66, 68, 84, 90, 95, 110, 114, 119]"""

def divisors_sum(n):
    """Calculate the sum of divisors of a number."""
    sum_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors

def prime_factors_sum(n):
    """Calculate the sum of prime factors of a number with multiplicities."""
    sum_factors = 0
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            sum_factors += divisor
            n //= divisor
        divisor += 1
    if n > 1:  # If n is a prime number greater than 1
        sum_factors += n
    return sum_factors

def ds_multof_pfs(nMin, nMax):
    """Find numbers in the range [nMin, nMax] where the sum of divisors is divisible by the sum of prime factors."""
    result = []
    for n in range(nMin, nMax + 1):
        sum_div = divisors_sum(n)
        sum_prime_factors = prime_factors_sum(n)
        
        if sum_div % sum_prime_factors == 0:
            result.append(n)
    
    return result

nMin = int(input("Enter the lower limit (nMin): "))
nMax = int(input("Enter the upper limit (nMax): "))

result = ds_multof_pfs(nMin, nMax)
print("Numbers satisfying the condition:", result)
