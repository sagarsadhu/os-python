def another_function():
    print("In another function")


def fun_challenge(lis):
    a = 10  # O(1)
    a = 50 + 3  # O(1)

    # the below loop is O(n) (loops are linear time)
    for i in range(0, len(lis)):
        another_function()  # O(n)
        stranger = True  # O(n)
        a += 1   # O(n)

    return a    # O(1)


lis = list(range(100))

print(fun_challenge(lis))


# The big O is O(3 + 4n)
