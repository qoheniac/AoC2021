# read starting positions and set win counters to zero
with open("input") as f:
    p1, p2 = [int(line.rstrip().split(": ")[1]) for line in f]
v1 = v2 = 0

# number of universes for possible outcomes of three die rolls
results = dict()
for roll1 in range(1, 4):
    for roll2 in range(1, 4):
        for roll3 in range(1, 4):
            result = roll1 + roll2 + roll3
            if result in results:
                results[result] += 1
            else:
                results[result] = 1


# player 1 rolls the die
def player1(p1, p2, s1=0, s2=0, universes=1):
    for r, u in results.items():
        p = (p1 + r - 1) % 10 + 1
        s = s1 + p
        u *= universes
        if s >= 21:
            global v1
            v1 += u
        else:
            player2(p, p2, s, s2, u)


# player 2 rolls the die
def player2(p1, p2, s1, s2, universes):
    for r, u in results.items():
        p = (p2 + r - 1) % 10 + 1
        s = s2 + p
        u *= universes
        if s >= 21:
            global v2
            v2 += u
        else:
            player1(p1, p, s1, s, u)


# start the game and output the higher win counter
player1(p1, p2)
print(max(v1, v2))
