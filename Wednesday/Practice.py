from tkinter.constants import BROWSE


def fabi(n):
    fib = []
    a , b = 0, 1

    for _ in range(n):
        fib.append(a)
        a, b = b, a+b
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(i):
            print(fib[j], end=" ")
        print()
if __name__ == "__main__":
    BROWSE=int(input("Enter a number: "))
    fabi(BROWSE)