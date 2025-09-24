def leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
def main():
    user_input = input("Enter a year: ")
    if user_input.isdigit():
        year = int(user_input)
        if leap_year(year):
            print(f"{year}, is a leap year")
        else:
            print(f"{year}, is not a leap year")

    else:
        print("enter a valid year")
if __name__ == "__main__":
 main()
