
a=4
b=3
mayor= 0
while a< 4 or b< 20 :
    if a > b:
        mayor=a
    elif b> a:
        mayor=b
    else:
        mayor=0
    a=a+mayor
    b=b+mayor
print(f"{a} {b}")