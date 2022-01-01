# situation defining parameters
junctions = {"A": 2, "B": 4, "C": 6, "D": 8}
energies = {"A": 1, "B": 10, "C": 100, "D": 1000}
hallway_length = 11


# possible moves for amphipod depending on configuration
def possible_moves(amphipod, configuration):

    # on hallway
    if amphipod[1] == "hallway":
        bottom_location_blocked = False
        left, right = sorted([amphipod[2], junctions[amphipod[0]]])
        for other in configuration:

            # check if other amphipod blocks way to correct room
            if other[1] == "hallway" and other[2] > left and other[2] < right:
                return []

            # check if destination room occupancy
            elif other[1] == amphipod[0]:
                if other[2] == 0 or other[0] != other[1]:
                    return []
                else:
                    bottom_location_blocked = True

        # calculate requisite energy and return destination
        steps = abs(junctions[amphipod[0]] - amphipod[2])
        if bottom_location_blocked:
            return [(amphipod[0], 0, (steps + 1) * energies[amphipod[0]])]
        else:
            return [(amphipod[0], 1, (steps + 2) * energies[amphipod[0]])]

    # in room
    else:

        # check if antipod already arrived
        if amphipod[1] == amphipod[0]:
            at_destination = True
            for other in configuration:
                if other[1] == amphipod[1] and other[0] != amphipod[0]:
                    at_destination = False
            if at_destination:
                return []

        # mark-off accessible hallway segment
        maxleft = 0
        minright = hallway_length - 1
        for other in configuration:
            if other[1] == "hallway":
                if other[2] < junctions[amphipod[1]]:
                    maxleft = max(maxleft, other[2] + 1)
                else:
                    minright = min(minright, other[2] - 1)

            # check if exit is blocked
            elif other[1] == amphipod[1] and other[2] < amphipod[2]:
                return []

        # collect possible destinations, calculate required energy and return
        destinations = []
        for location in range(maxleft, minright + 1):
            if location not in junctions.values():
                steps = (
                    abs(location - junctions[amphipod[1]]) + 1 + amphipod[2]
                )
                destinations.append(
                    ("hallway", location, steps * energies[amphipod[0]])
                )
        return destinations


# read input file
with open("input") as f:
    burrow = f.read().split("\n")

# parse input file and collect amphipods as (kind, room, location) tuples
start_configuration = []
for i, kind in enumerate(burrow[1]):  # parse hallway
    if kind in ["A", "B", "C", "D"]:
        start_configuration.append((kind, "hallway", i - 1))
for room, j in junctions.items():  # parse rooms
    for i in range(2):
        if (kind := burrow[2 + i][1 + j]) in ["A", "B", "C", "D"]:
            start_configuration.append((kind, room, i))
start_configuration = tuple(start_configuration)

# initialization for Dijkstra-like algorithm to find lowest energy
total_energy = {start_configuration: 0}
to_visit = set([start_configuration])

# visit configuration with lowest total energy to get there
while True:
    lowest_energy = float("inf")
    for configuration in to_visit:
        if total_energy[configuration] < lowest_energy:
            lowest_energy = total_energy[configuration]
            lowest_energy_configuration = configuration
    to_visit.remove(lowest_energy_configuration)
    print(lowest_energy, end="\r")

    # quit if configuration equals desired configuration
    for new_amphipod in lowest_energy_configuration:
        if new_amphipod[0] != new_amphipod[1]:
            break
    else:
        print(lowest_energy)
        break

    # get neighbor configurations and energies to get there
    for amphipod in lowest_energy_configuration:
        for destination in possible_moves(
            amphipod, lowest_energy_configuration
        ):

            # construct neighbor configuration and calculate the total energy
            new_configuration = tuple(
                other
                if other != amphipod
                else (amphipod[0], destination[0], destination[1])
                for other in lowest_energy_configuration
            )
            new_configuration_energy = lowest_energy + destination[2]

            # if neighbor configuration not considered yet, add it to to_visit
            if new_configuration not in total_energy:
                to_visit.add(new_configuration)

            # update energy for neighbor configuration if smaller than before
            if (
                new_configuration not in total_energy
                or new_configuration_energy < total_energy[new_configuration]
            ):
                total_energy[new_configuration] = new_configuration_energy
