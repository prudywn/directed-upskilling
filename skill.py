a = [7, 1, 9, 6, 10, 5, 8, 2, 3, 4]
def shift_numbers(a, t):
    for j in (1, t):
        x = a[1]
        for i in (1, len(a)-1):
            a[i] = a[i+1]
        a[len(a)] = x

    for i in (1, len(a)):
        if i == len(a):
            print(a[i])
        else:
            print(a[i], ", ")


shift_numbers(a, 5)