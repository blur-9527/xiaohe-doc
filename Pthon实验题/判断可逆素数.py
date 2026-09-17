# 判断一个数是否为素数的函数
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 判断一个数是否为可逆素数的函数
def is_reversible_prime(num):
    if not is_prime(num):
        return False
    reversed_num = int(str(num)[::-1])
    return is_prime(reversed_num)


num = int(input())
if is_reversible_prime(num):
    print("yes")
else:
    print("no")

    



