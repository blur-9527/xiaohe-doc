# 读取输入
weight, height = map(float, input().split())

# 计算BMI
bmi = weight / (height ** 2)

# 根据BMI值进行分类
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

# 输出结果
print(f"{bmi:.2f} {category}")

