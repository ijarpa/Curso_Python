from math import ceil as ceil

#number_1 = int(input("the number of manufactured items: "))
#number_2 = int(input("the number of items that the user will pack per box:"))

#print(ceil(number_1/ number_2))

################# ################### ###################

def boxes(x, y):
    print(ceil(x/ y))

x = int(input("the number of manufactured items: "))
y = int(input("the number of items that the user will pack per box: "))

boxes(x, y)

