def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range (2, num-1):

        if num % i == 0:
            return False
    return True

is_prime(num)