list_1 = [1, 2, 3, 4, 5]


def array_pairs(input_list):
    for item in input_list:

        for num in range(0, len(list_1)):
            print(item, list_1[num])


#array_pairs(list_1)


def numbers_and_pair_sums(input_list):
    for num in input_list:
        print(num)

    for item in input_list:

        for num in range(0, len(list_1)):
            print(item + list_1[num])


numbers_and_pair_sums(list_1)
