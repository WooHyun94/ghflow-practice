dic = {0:0, 1:1}

def fibo(n):
    global dic
    if n in dic:
        return dic[n]
    dic[n] = fibo(n - 1) + fibo(n - 2)
    return dic[n]

print(fibo(5))
