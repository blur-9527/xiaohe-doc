# 读取输入
area = input().strip()
severity = input().strip()
trapped = input().strip()

# 判断响应级别
if severity in ['High', 'Medium']:
    if trapped == 'Yes':
        response = 'Level 1 Response'
    else:
        response = 'Level 2 Response'
else: # Low
    if trapped == 'Yes':
        response = 'Level 4 Response'
    else:
        response = 'Level 3 Response'

# 输出结果
print(response)

