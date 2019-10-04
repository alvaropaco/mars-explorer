import sys

from probe import Probe


def main():
    steps = "5 5 1 2 N LMLMLMLMM 3 3 E MMRMMRMRRM".split(" ")
    next_probe = 1   
    
    map_w = steps[0]
    map_h = steps[1]

    for idx, line in enumerate(steps):
        if idx > next_probe:
            probe = Probe(map_w, map_h, steps[idx], steps[idx + 1], steps[idx + 2])
            probe.explore(steps[idx +3])
            next_probe = idx + 3
            str(probe)

if __name__ == '__main__':
    main()