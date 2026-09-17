def calculate_risk(device_risk, operation_risk, environment_risk):
    total_risk = device_risk + operation_risk + environment_risk
    if total_risk < 15:
        return "Low Risk"
    elif 15 <= total_risk < 25:
        return "Medium Risk"
    else:
        return "High Risk"

# 获取用户输入
device = int(input())
operation = int(input())
environment = int(input())

# 计算并输出风险等级
risk_level = calculate_risk(device, operation, environment)
print(risk_level)    
