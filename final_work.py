array = [1, 3, 4, 7, 8, 10, 11, 15, 19, 21]

number = int(input("Input number you want to find - "))

left = 0
right = len(array) - 1
mid = right // 2


while True:
    if array[mid] == number:
        print(mid)
        break
    elif array[mid] > number:
        left = mid
        mid = (right - left) // 2
    elif array[mid] < number:
        left = mid
        mid = ((right + left) // 2) + 1



