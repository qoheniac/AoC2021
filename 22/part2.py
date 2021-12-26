from trimesh import Trimesh
from trimesh.creation import box
from trimesh.transformations import translation_matrix
from tqdm import tqdm


def parse_limits(limits):
    center = [0] * 3
    extent = [0] * 3
    for i, dimension in enumerate(limits.split(",")):
        interval = dimension.split("=")[1]
        lower, upper = [int(number) for number in interval.split("..")]
        center[i] = (upper + lower) / 2
        extent[i] = 1 + upper - lower
    return box(extent, translation_matrix(center))


mesh = Trimesh(process=False)
with open("input") as f:
    steps = [line.split(" ") for line in f.read().split("\n")[:-1]]
for step in tqdm(steps):
    if step[0] == "on":
        mesh = mesh.union(parse_limits(step[1]), engine="scad")
    else:
        mesh = mesh.difference(parse_limits(step[1]), engine="scad")
print(int(mesh.volume))
