x = [1, 2, 3, 4, 5, 6, 11]
y = [4, 5, 6, 7, 8, 9, 10]
z = [10.5, 11.5, 12.5, 13.5]

def average(lst):
    total = 0
    for i in lst:
        total = total + i
    ave = total/ len(lst)
    return ave
print(average(x))
print(average(y))
print(average(z))
