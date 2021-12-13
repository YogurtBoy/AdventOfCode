import time
start_time = time.time()

# f = open("caves_tiny.txt", "r")
# f = open("caves_small.txt", "r")
f = open("caves.txt", "r")
if f:
    print("Successfully opened data...")

class Tunnel:
    def __init__(self):
        self.caves = ['', '']
        self.branches = []
    
    def isStart(self):
        if self.caves[0] == 'start' or self.caves[1] == 'start':
            return True
        else:
            return False
    
    def isEnd(self):
        if self.caves[0] == 'end' or self.caves[1] == 'end':
            return True
        else:
            return False
    
    def isConnection(self, cave):
        if cave == self.caves[0] or cave == self.caves[1]:
            return True
        else:
            return False
    
    def isOnEndOfRoute(self, routeStr):
        if self.caves[0][-2] == routeStr[-2] and self.caves[0][-1] == routeStr[-1]:
            return 0
        elif self.caves[1][-2] == routeStr[-2] and self.caves[1][-1] == routeStr[-1]:
            return 1
        else: 
            return -1 

    def makeConnection(self, tunnelMap):
        for ii in range(len(tunnelMap)):
            if self.isConnection(tunnelMap[ii].caves[0]) and not tunnelMap[ii].isConnection('start'): 
                self.branches.append(ii)
            elif self.isConnection(tunnelMap[ii].caves[1]) and not tunnelMap[ii].isConnection('start'):
                self.branches.append(ii)
        return self

    def printTunnel(self):
        print(str(self.caves[0]) + " <--> " + str(self.caves[1]))

def hasTinyCaveBeenVisited(cave, route):
    if ord(cave[0]) < 97:
        return 0
    elif route.find(cave) > -1:
        # For part 1 answer, remove everything having to do with this extra if statement and the 'v'
        if route[0] == 'v':
            return 1
        else:
            return -1
    else: 
        return 0

def explore(nel, system, routeList, iDx):
    for ii in nel.branches:

        cunTun = system[ii]
        
        caveIdx = cunTun.isOnEndOfRoute(routeList[iDx])
        if caveIdx > 0:
            if hasTinyCaveBeenVisited(cunTun.caves[0], routeList[iDx]) < 1:
                routeList.insert(iDx + 1, '')
                routeList[iDx + 1] = routeList[iDx + 1] + routeList[iDx] + cunTun.caves[0]
                if hasTinyCaveBeenVisited(cunTun.caves[0], routeList[iDx]) < 0:
                    routeList[iDx + 1] = 'v' + routeList[iDx + 1]
                if routeList[iDx + 1].find('end') < 0:
                    routeList = explore(cunTun, system, routeList, iDx + 1)
                else:
                    continue
        elif caveIdx > -1:
            if hasTinyCaveBeenVisited(cunTun.caves[1], routeList[iDx]) < 1:
                routeList.insert(iDx + 1, '')
                routeList[iDx + 1] = routeList[iDx + 1] + routeList[iDx] + cunTun.caves[1]
                if hasTinyCaveBeenVisited(cunTun.caves[1], routeList[iDx]) < 0:
                    routeList[iDx + 1] = 'v' + routeList[iDx + 1]
                if routeList[iDx + 1].find('end') < 0:
                    routeList = explore(cunTun, system, routeList, iDx + 1)
                else:
                    continue
        
    routeList.pop(iDx)
    
    return routeList

# A at 65
# Z at 90
# a at 97 
# z at 122

system = []
for line in f:
    connection = line.strip().split('-')
    system.append(Tunnel())
    system[-1].caves = [connection[0], connection[1]]
for tun in system:
    tun = tun.makeConnection(system)

routes = []
for ii in range(len(system)):
    tun = system[ii]
    if tun.isStart():
        routes.append('start')
        if tun.caves[0] == 'start':
            routes[-1] = routes[-1] + tun.caves[1]
        else:
            routes[-1] = routes[-1] + tun.caves[0]
        routes = explore(tun, system, routes, len(routes) - 1)

print(routes)
print(len(routes))
            

