from random import choice, shuffle

def gen_password(n: int):
    digits = "0123456789"
    symbols = "!@#$%^&*()[]{}\|/?><,.`~"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()[]{}\|/?><,.`~0123456789"
    a = []
    if n > 2:
        a.append(choice(digits))
        a.append(choice(symbols))
        n -= 2
    for _ in range(n):
        a.append(choice(alphabet))
    shuffle(a)
    p = "".join(a)
    print(p)
    return p

if __name__ == "__main__":
    gen_password(int(input("Please enter password length: ")))
