opening = ["(", "[", "{", "<"]
closing = [")", "]", "}", ">"]
points = [1, 2, 3, 4]
scores = []
with open("input") as f:
    for line in f:
        memory = []
        for character in list(line):
            for i, c in enumerate(opening):
                if c == character:
                    memory.append(i)
                    break
            else:
                for i, c in enumerate(closing):
                    if c == character:
                        if c == closing[memory[-1]]:
                            memory.pop()
                        else:
                            break
                else:
                    continue
                break
        else:
            score = 0
            for i in memory[::-1]:
                score *= 5
                score += i + 1
            scores.append(score)
print(sorted(scores)[len(scores) // 2])
