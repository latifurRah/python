num = int(input("take num: "))
for i in range(2,num):
    if num/i != 0:
        continue
    elif num/i == 0:
        print("n p")
    print("p")