# read risk levels
with open("input") as f:
    risk = [[int(num) for num in line.rstrip()] for line in f]
rows, cols = len(risk), len(risk[0])

# initialization for Dijkstra-like algorithm to find lowest risk
total = [[float("inf")] * rows for _ in range(cols)]
total[0][0] = 0
tovisit = set([(0, 0)])
while True:

    # visit location with lowest risk to get there
    total_min = float("inf")
    for i, j in tovisit:
        if total[i][j] < total_min:
            total_min = total[i][j]
            i_min, j_min = i, j
    tovisit.remove((i_min, j_min))

    # calculate total risk to visit neighbors through this path
    for Δi, Δj in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
        ni, nj = i_min + Δi, j_min + Δj
        if ni >= 0 and ni < rows and nj >= 0 and nj < cols:
            alt = total[i_min][j_min] + risk[ni][nj]

            # quit if neighbor equals destination
            if (ni, nj) == (rows - 1, cols - 1):
                print(alt)
                break

            # if neighbor not considered yet, save risk and add to tovisit
            if total[ni][nj] == float("inf"):
                total[ni][nj] = alt
                tovisit.add((ni, nj))

            # else if smaller update neighbors total risk to get there
            elif alt < total[ni][nj]:
                total[ni][nj] = alt

    # leave while loop if destination was reached
    else:
        continue
    break
