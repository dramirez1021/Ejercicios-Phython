def v_s (str):
    r=""
    for i in range(len(str)):
        if i %2 == 0:
            r = r + str[i]
    return r
print(v_s("abcdef"),end=" ")
print(v_s("python"),end=" ")