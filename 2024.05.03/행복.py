N = int(input())

score = str(input())
sco = []

for i in score.split():
    sco.append(int(i))

print(max(sco) - min(sco))