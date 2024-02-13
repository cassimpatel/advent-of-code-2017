def parse_input(input):
    for repr in ['p=<', 'v=<', 'a=<', '>', ' ']:
        input = input.replace(repr, '')
    particles = [[int(y) for y in x.split(',')] for x in input.split('\n')]
    return particles

def day11_part1(input):
    particles = parse_input(input)

    # calculate the manhattan acceleration, velocity and position
    summarised = []
    for [px, py, pz, vx, vy, vz, ax, ay, az] in particles:
        a = abs(ax) + abs(ay) + abs(az)
        v = abs(vx) + abs(vy) + abs(vz)
        p = abs(px) + abs(py) + abs(pz)
        summarised.append((a, v, p))

    # sort by a then v then p, get the indices of the particles
    res = sorted(range(len(summarised)),key=summarised.__getitem__)
    return res[0]

def day11_part2(input):
    particles = parse_input(input)

    # guess 1000 steps is enough
    for _ in range(1000):
        # map positions to list of particle indices
        positions = {}

        # for each particle, apply movement, store new position
        for i in range(len(particles)):
            particles[i][3] += particles[i][6]
            particles[i][4] += particles[i][7]
            particles[i][5] += particles[i][8]
            particles[i][0] += particles[i][3]
            particles[i][1] += particles[i][4]
            particles[i][2] += particles[i][5]
            
            p = tuple(particles[i][:3])
            if p not in positions:
                positions[p] = []
            positions[p].append(i)
        
        # create list of indices to remove, sort descending to correctly delete from particles
        to_remove = []
        for matches in positions.values():
            if len(matches) == 1: continue
            for v in matches:
                to_remove.append(v)
        to_remove.sort(reverse=True)
        for i in to_remove:
            particles.pop(i)

    return len(particles)

if __name__ == "__main__":
    example_input_1 = open('example_1.txt', 'r').read()
    example_input_2 = open('example_2.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day11_part1(example_input_1) == 0
    print(day11_part1(test_input))

    assert day11_part2(example_input_2) == 1
    print(day11_part2(test_input))