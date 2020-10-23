sentence = input().split()

for i in range(len(sentence)):
    if sentence[i] == ' ':
        del sentence[i]

print(len(sentence))
