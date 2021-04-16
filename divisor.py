from math import sqrt

def find_divisors(n: int):
    upper_bound = int(n/2)
    divisors = {x if n % x == 0 else 0 for x in range(2, upper_bound+1)}
    divisors.discard(0)
    print(list(divisors))
    return divisors

if __name__ == "__main__":
    find_divisors(int(input("Enter number: ")))
