def booooo(n):
    for i in range(0, len(n)):
        print('booooooooo!')


booooo([1, 2, 3, 4, 5])  # O(1)


def n_times_hi(n):
    hi = []
    for i in range(n):
        hi.append('hi!')

    return hi


print(n_times_hi(6))  # o(n)




