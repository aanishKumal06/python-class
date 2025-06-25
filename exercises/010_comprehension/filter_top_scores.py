# Write a Python program using dictionary comprehension to filter Nepali students who scored more than 80 marks.

scores = {
    'Sita': 85,
    'Ram': 72,
    'Gita': 90,
    'Hari': 65,
    'Ayush': 95
}

top_scores = {name: score for name, score in scores.items() if score > 80}

for name, score in top_scores.items():
    print(f"{name}: {score}")
