# # 1 problem 
# # f string

# num=int(input("Enter the num::"))
# for i  in range(1,11):
#     print(f"{i}*{num}={i*num}")
#2222222222222222

# ls=["sabbir","sohag","saurav","'latif","hafiz"]
# for i in ls:
#     if i[0]=="S" or i[0]=="s":
#         print(f"bad morning {i}")

# #3
# num=int(input("Enter the num:::"))
# i=1
# while i<=10:
#     print(f"{i}X{num}={i*num}")
#     i=i+1
############---------4----------
num=int(input("Enter the num::"))
# if num%2==0:
#     print("prime")
# else:
#     print("Non prime")
flag=True
if num<2:
    print("Non prime")
else:
    for i in range(2,num):
        if num==2:
            print("prime")
            break
        if num%i==0:
            flag=False
            break
    if flag:
        print("prime")
    else:
        print("non prime")