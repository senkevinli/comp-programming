global parent
global size
global people

def initialize(n):
    parent = [i for i in range(n)] # parent labels
    size = [1 for _ in range(n)]   # size (i.e. number of cars)
    people = [0 for _ in range(n)] # number of people in car


def find(child):
    if parent[child] == child :
        return child

    parent[child] = find(parent[child])
    return parent[child]

def getPeople(child):
    return people[find(child)]

def union(childA, childB) :
    rootA = find(childA)
    rootB = find(childB)

    if (rootA == rootB):
        # Already same component, no need to merge
        return

    if (size[rootA] > size[rootB]):
        # Swap
        rootA, rootB = rootB, rootA

        # We have that size[rootA] <= size[rootB], so it is best to merge rootA into
        # rootB
        size[rootB] += size[rootA]
        parent[rootA] = rootB
        people[rootB] += people[rootA]