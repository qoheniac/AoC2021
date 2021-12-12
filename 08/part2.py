result = 0
with open("input") as f:
    for line in f:
        patterns, output = [
            list(map(set, half.split())) for half in line.split(" | ")
        ]
        patterns = sorted(patterns, key=len)
        codes = [None] * 10

        # unique digits 1, 4, 7 and 8
        codes[1] = patterns[0]
        codes[7] = patterns[1]
        codes[4] = patterns[2]
        codes[8] = patterns[9]

        # find six-segment digits 0, 6 and 9
        for i in range(6, 9):
            pattern = patterns[i]
            if codes[4].issubset(pattern):
                codes[9] = pattern
            elif codes[1].issubset(pattern):
                codes[0] = pattern
            else:
                codes[6] = pattern

        # find five-segment digits 2, 3 and 5
        for i in range(3, 6):
            pattern = patterns[i]
            if codes[1].issubset(pattern):
                codes[3] = pattern
            elif len(codes[6] - pattern) == 2:
                codes[2] = pattern
            else:
                codes[5] = pattern

        # decode output
        number = 0
        for order, digit_code in enumerate(output[::-1]):
            for digit, code in enumerate(codes):
                if code == digit_code:
                    number += digit * 10 ** order
                    break
        result += number
print(result)
