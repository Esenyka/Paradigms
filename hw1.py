from random import randint


def sort_list_imperative(numbers):
    count = len(numbers)
    while count != 0:
        for i in range(count - 1):
            num1 = numbers[i]
            num2 = numbers[i + 1]
            if num1 < num2:
                numbers[i] = num2
                numbers[i + 1] = num1
        count -= 1

    return numbers


def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


f = [randint(0, 55) for i in range(10)]
print(sort_list_declarative(f))
print(sort_list_imperative(f))