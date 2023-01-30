def get_prime_factors (num):
    index = 2
    prime_factors = []
    while num > 1:
        if (num % index) == 0:
            prime_factors.append(index)
            num = num / index
        else:
            index = index + 1
    return (prime_factors)