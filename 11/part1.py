# octopus class containing energy, neighbors and flash logic
class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashed = False
        self.neighbors = []

    def charge(self):
        self.energy += 1
        if not self.flashed and self.energy > 9:
            self.flash()

    def flash(self):
        self.flashed = True
        for octopus in self.neighbors:
            octopus.charge()


# read input and initialize octopusses
with open("input") as f:
    octopusses = [
        [Octopus(int(num)) for num in list(line.rstrip())]
        for line in f.readlines()
    ]
rows = len(octopusses)
cols = len(octopusses[0])

# introduce octopusses to their neighbors
for i in range(rows):
    for j in range(cols):
        for Δi in range(-1, 2):
            for Δj in range(-1, 2):
                if Δi != 0 or Δj != 0:
                    ni, nj = i + Δi, j + Δj
                    if ni >= 0 and ni < rows and nj >= 0 and nj < cols:
                        octopusses[i][j].neighbors.append(octopusses[ni][nj])

# count flashes after 100 steps
count = 0
for _ in range(100):
    for row in octopusses:
        for octopus in row:
            octopus.charge()
    for row in octopusses:
        for octopus in row:
            if octopus.flashed:
                octopus.energy = 0
                octopus.flashed = False
                count += 1
print(count)
