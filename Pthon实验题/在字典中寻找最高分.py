
names_input = input().strip()
scores_input = input().strip()

# 处理姓名和分数
names = [name.strip() for name in names_input.split(',')]
scores = [int(score.strip()) for score in scores_input.split(',')]

# 组合成字典
score_dict = dict(zip(names, scores))

# 找出最高分的学生
max_score = max(score_dict.values())
max_student = [name for name, score in score_dict.items() if score == max_score][0]

# 输出结果
print(f"{max_student}, {max_score}")

