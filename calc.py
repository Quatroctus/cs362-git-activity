def calc(a, b):
    results = [a+b, a-b, a*b, a/b]
    for a in results:
        print(a)
    sum_of_list = sum(results)
    print(sum_of_list)

if __name__ == "__main__":
    calc(float(input("Please enter the first number: ")), float(input("Please enter the second number: ")))
