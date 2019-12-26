#section A question 2
'''integer = int(input("please enter an integer "))
num = 1
while integer >= 0:
    print(integer)
    integer -= num
    num += 1'''
    


#section A question 1
'''int1 = int(input("please enter an integer "))
int2 = int(input("please enter another integer "))
if int1 < int2:
    for num in range(1, int2, 1):
        square = int1 ** num
        if square < int2:
            print(square)
            num += 1    
else:
    for num in range(1, int1, 1):
        square = int2 ** num
        if square < int1:
            print(square)
            num += 1''' 




#section A question 3
'''integer = int(input("please enter a positive integer "))
total = 0
product = 1
for num in range(1, integer + 1, 1):
    root = num ** (1/2)
    print("square root of", num, "=", format(root, ".3f"))
    total += root
    product *= root
print("sum of square roots: ", format(total, ".2f"))
print("product of square roots: ", format(product, ".2f"))'''



#section A question 5
'''import random
total_red = 0
total_blue = 0
total_white = 0
integer = int(input("please enter a positive integer "))
for num in range(1, integer + 1, 1):
    rand = random.randint(1, 3)
    if rand == 1:
        print("red")
        total_red += 1 
    elif rand == 2:
        print("blue")
        total_blue += 1
    else:
        print("white")
        total_white += 1
print("reds", total_red, "blues", total_blue, "whites", total_white)'''









