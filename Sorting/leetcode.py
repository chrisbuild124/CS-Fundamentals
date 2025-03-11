def criticalConnections(n, connections):
    # n is number of connections (n-1) numbered
    # connections[i] = [ai, bi]
    noRepeats = set()
    visited = set()
    for i in range(len(connections)):
        for j in range(2):
            if connections[i][j] not in noRepeats:
                noRepeats.add(connections[i][j])
                visited.add(connections[i][j])
            elif connections[i][j] in visited and connections[i][j] in noRepeats:
                noRepeats.remove(connections[i][j])
    
    returnList = []
    for i in range(len(connections)):
        for j in range(2):
            if connections[i][j] in noRepeats:
                returnList.append(connections[i])
                break

    return returnList

print(criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
