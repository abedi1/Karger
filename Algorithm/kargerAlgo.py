# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Aman Bedi

import random, copy

#input can be any adjacency list in a text file
data = open("testCase.txt", "r")
G = {}
for line in data:
    lst = [int(s) for s in line.split()]  # creates a list for each line of text file
    G[lst[0]] = lst[1:]  # adds the list for one vertex to the entire adj list in G
    # The code that creates an adjacency list from a text file(lines 6-10) were done with help from online resources


def choose_random_key(G):
    a = random.choice(list(G.keys()))  # picks a random vertex
    b = random.choice(list(G[a]))  # picks a random edge in the adjacency list
    return a, b


def karger(G):
    length = []
    while len(G) > 2:
        a, b = choose_random_key(G)  # the nodes that are part of the random edge
        G[a].extend(G[b])  # copies all items
        for x in G[b]:
            G[x].remove(b)  # remove the other occurrences of b in adjacency list
            G[x].append(a)  # tell them to look at a instead
        while a in G[a]:
            G[a].remove(a)  # remove self loops
        del G[b]  # getting rid of the empty vertex from the adj list
    return len(G[a])  # length of either vertex is same so just picked a


def multipleKarger(iterations):
    i = 0
    count = 10000000000  # a very large number that isn't a possible mincut
    while i < iterations:
        data = copy.deepcopy(G)  # this way don't have to reread the txt file
        min_cut = karger(data)
        if min_cut < count:
            count = min_cut
        i = i + 1
    return count


print("Running Karger one time: ", multipleKarger(1))
print("Running Karger one time: ", multipleKarger(1))
print("Running Karger 100 times: ", multipleKarger(100))
