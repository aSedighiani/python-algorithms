from prime_factors import *
def common_prime_factors(a,b):
    if a < b:
        for i in range(a,0,-1):
            if a % i == 0 and b % i == 0:
                cf = get_prime_factors(i)
                return cf
    elif a > b:
        for r in range(b,0,-1):
            if a % r == 0 and b % r == 0:
                cf = get_prime_factors(r)
                return cf
    elif a == b:
        cf = get_prime_factors(a)
        return cf