def main():
    print('Hello world!')

    # a = list(range(1,6))
    a = [1, 2, 3, 4, 5]
    # b = list(range(1,10,2))
    b = [1, 3, 5, 7, 9]
    # c = list(range(4,9))
    c = [4, 5, 6, 7, 8]

    print(manipulate_arr(a))
    print(manipulate_arr(b))
    print(manipulate_arr(c))

    print(epsilon(5))

    easy_dict = {'Easy': 'Dictionary'}
    print(easy_dict)


def manipulate_arr(num_list):
    new_list = [num + 1 for num in num_list]
    return new_list


def epsilon(i):
    total = 0
    for x in range(i + 1):
        total += x

    return total


if __name__ == "__main__":
    main()
