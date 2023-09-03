def is_prime_number(n):
    if n <= 1:
        return False

    divisors = 2
    while divisors < n:
        if n % divisors == 0:
            return False
        divisors += 1

    return True

number = int(input("Enter a positive integer: "))

if is_prime_number(number):
    print("This number is prime")
else:
    print("This number is not prime")
