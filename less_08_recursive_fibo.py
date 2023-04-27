import time

def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)
def fibo_optim2(num):

    fibo_num = {}

    def fibo_optim(num):
        if num in fibo_num:
            return fibo_num[num]
        elif num == 0:
            fibo_num[num] = 0
            return fibo_num[num]
        elif num == 1:
            fibo_num[num] = 1
            return fibo_num[num]
        else:
            fibo_num[num] = fibo_optim(num-1) + fibo_optim(num-2)
            return fibo_num[num]
    return fibo_optim(num)

start = time.time()
for i in range (0, 100, 1):
    result = fibo_optim2(i)
    print(i, result)

end = time.time()
result_time = end - start
print(i, result, result_time)
