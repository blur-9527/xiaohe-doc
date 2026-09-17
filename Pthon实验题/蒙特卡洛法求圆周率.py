import random

def estimate_pi(n):
    random.seed(12345)  # 设置随机种子以确保结果可重现
    inside = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    return 4 * inside / n

# 获取用户输入
n = int(input())

# 计算并输出估计的π值
pi_estimate = estimate_pi(n)
print(f"{pi_estimate:.6f}")    
