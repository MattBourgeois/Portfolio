# from itertools import count


mylist = [5]
num = 0
def countdown():
    while num is not  0:
        num -= 1
        mylist.append(num)

countdown()