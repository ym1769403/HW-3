#Yasir Mushtaque
#1769403

list = input()


list_val = [int(val) for val in list.split() if int(val) >= 0]

list_val.sort()

for val in list_val:
    print(val,end = ' ')