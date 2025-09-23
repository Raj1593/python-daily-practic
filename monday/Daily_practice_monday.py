# def basic_calc(num1, num2):
#     return num1 + num2
# print(basic_calc(1, 2))
from itertools import count


# def data_struct():
#     my_list = [1, 2, 3, 4, 5, "a", "b", 0]
#     print(my_list[3])  # 4
#
#     my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#     print(my_dict['c'])  # 3
#
#     my_tuple = (1, 2, 3, 4)
#     print(my_tuple[2])  # 3
#
#     if my_list == list(my_tuple):
#         print("List is equal to tuple (as list)")
#     else:
#         print("List is not equal to tuple")
# data_struct()


from collections import Counter
def my_list():
    list_data = [1, 2, "d", 4, 5,"a"]
    counts=Counter(list_data)
    print(counts)
    print(counts.most_common(2))
    total=len(list_data)
    return list_data

def my_tuple():
    tuple_data = (1, 2, "d", 4, 5,"a")
    counts=Counter(tuple_data)
    print(counts)
    return tuple_data
def my_dict():
    dict_data = {1,3,4,5,"a"}
    counts=Counter(dict_data)
    return dict_data

def compare(list_data, tuple_data, dict_data):
    if (list_data) == (tuple_data):
        print("list and tuple are equal")
    elif len(list_data) > len(tuple_data):
        print("list is greater than tuple")
    elif len(list_data) < len(tuple_data):
        print("list is less than tuple")
    elif len(list_data) == len(dict_data):
        print("dictionary is equal")
    elif len(tuple_data) == len(dict_data):
        print("tuple is equal")
    else:
        print("tuple is greater than dictionary")

def main():
    my_list()
    my_tuple()
    my_dict()
    compare(my_list(), my_tuple(), my_dict())
if __name__ == '__main__':
    main()