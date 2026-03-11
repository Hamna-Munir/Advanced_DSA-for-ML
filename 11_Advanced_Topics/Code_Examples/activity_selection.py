# Greedy Algorithm Example
# Activity Selection Problem

def activity_selection(start, finish):

    activities = []
    i = 0
    activities.append(i)

    for j in range(1, len(start)):
        if start[j] >= finish[i]:
            activities.append(j)
            i = j

    return activities


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

print("Selected activity indices:", activity_selection(start, finish))


# Output
# Selected activity indices: [0, 1, 3, 4]
