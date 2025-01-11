chat_score = int(input('Введи показатель по чатам: '))  # 100% for chats
chat_weight = 0.2  # 20% weight

test_score = int(input('Введи показатель по тесту: '))  # 100% for tests
test_weight = 0.3  # 30% weight

expert_score = int(input('Введи показатель по оценке QC: '))  # 93.16% expert evaluation
expert_weight = 0.5  # 50% weight

# Calculating the overall score
overall_score = (chat_score * chat_weight) + (test_score * test_weight) + (expert_score * expert_weight)
print(overall_score)