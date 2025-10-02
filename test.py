def smallest(numbers):
    x = True
    smallest = 0
    for number in numbers:
        if x:
            smallest = number
            x = False
        if number < smallest:
            smallest = number
    return smallest

smallest = smallest([-1,0,3,4,5,6,7,8,-9,10,11,12])
print(smallest)