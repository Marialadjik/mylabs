# TODO решите задачу
import json

def task() -> float:
    filename = 'input.json'  # Заменила на путь к JSON файлу
    with open(filename, 'r') as file:
        input = json.load(file)
    total_sum = 0.0

    for item in input:
        if 'score' in item and 'weight' in item:
            total_sum += item['score'] * item['weight']

    return round(total_sum, 3)

print(task())
