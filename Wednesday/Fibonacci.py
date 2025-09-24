from itertools import count


def fibonacci(n):
    fib = []
    a = 0
    b = 1
    for _ in range(n):
        fib.append(a)
        a,b = b,a+b
    for i in range(n):
        print(" " *(n -i -1), end=" " )
        for j in range(i):
            print(fib[j], end=" ")
        print()
if __name__ == "__main__":
 row= int(input("enter a row number: "))
 fibonacci(row)