# pass or fail of a student in class
a=77
b=80
c=90
if a>33 and b>33 and c>33:
    avg=(a+b+c)/3
    if avg>40:
        print("pass")
    else:
        print("fail")
else:
    print("fail")