list = ["Ada    Happy,Loving,Fuzzy,Big"]

def find_pet_dict(filename):
    d = {}
    with open (filename,'r') as f:
        for line in f:
            line = line.split()
            name = line[0]
            adj = line[1].split(",")
            if name not in d:
                d[name] = adj

        return d

def find_pets(d,adjectives):
    ans = []
    for name,adj in d.items():
        if adjectives in adj:
            ans.append(name)
    if len(ans) == 0:
        print("")
    else:
        print(",".join(ans))


def find_pet_dict2(list):
    for line in list:
        print(line)
        line = line.split()
        line2 = line[1].split(",")
        print(line)
find_pet_dict2(list)

for adj in adjs:
    if adj not in d:
        d[adj] = name
    else:
        d[adj].append(name)