def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1) 

print(factorial(5))

def sum_first_n_positive_nums(n):
    if n == 1:
        return 1
    else:
        return n + sum_first_n_positive_nums(n-1)
print(sum_first_n_positive_nums(4))

def power_of_two(n):
    count = 0
    if n == 1:
        return 'YES'
    elif n > 1 and n < 2:
        return 'NO'
    else:
        if n % 2 == 0:
            count+=1
            return power_of_two(n / 2)
        else:
            return 'NO'
    

print(power_of_two(10))