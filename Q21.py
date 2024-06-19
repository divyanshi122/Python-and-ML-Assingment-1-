def countX(lst, x):
    count = 0
    for i in lst:
        if (i == x):
            count = count + 1
    return count

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = int(input("Enter a number whose occurence you want to check in the list: "))
print('{} has occurred {} times'.format(x,countX(lst, x)))