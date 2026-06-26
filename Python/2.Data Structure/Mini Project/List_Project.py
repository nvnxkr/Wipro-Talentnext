n = int(input("Enter number of scores: "))

scores = []

for i in range(n):
    score = int(input("Enter score: "))
    scores.append(score)

scores = list(set(scores))
scores.sort()

print("Runner-up score:", scores[-2])