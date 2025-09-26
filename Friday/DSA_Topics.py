
# def largest_number(numbers):
#   unique = list(numbers)
#   unique.sort()
#   return unique[-1]
#
# numbers= [1,2,6,65,23,97,11,45]
# print(largest_number(numbers))

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))


