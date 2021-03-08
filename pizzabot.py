import re

class Pizzabot(object):

    def __init__(self, arg):
        self.arg = arg
        self.limits = []
        self.delivOrder = {}
        self.route = []
        self.botCurrent = [0,0]
        tmplist2 = []

# Load delivery orders as a dictionary
# The key is a horiz coordinate and values are corresponding vertical coordinates
# First, split the delivery part of input string into list
# Check if there are any delivery orders, if not - skip the rest of the process
        start = self.arg.find('(')
        if start > -1:
            tmplist1 = [int(i) for i in (re.split(r'[(),\s]\s*', self.arg[start:])) if i != '']

# Pair  elements into horiz and vert coordinates
            for i in range(0,len(tmplist1),2):
                tmplist2.append([tmplist1[i],tmplist1[i+1]])

# Find delivery area limits
            tmplist1 = [int(i) for i in (re.split(r'[x\s]\s*', self.arg[:start])) if i != '']
            self.limits.append(int(tmplist1[0]))
            self.limits.append(int(tmplist1[1]))

# Finally, build a delivery order dictionary
            for i in tmplist2:
                if i[0] in self.delivOrder:
                    self.delivOrder[i[0]].append(i[1])
                else:
                    self.delivOrder[i[0]] = [i[1]]

# Run pizzabot until all deliveries are done
    def runPizzabot(self):

        # Deliver pizza along a vertical axis
        def deliverRow(i,botCurrent):
                    self.i = i
                    self.botCurrent = botCurrent

        # Sort delivery orders along a vertical axis for better efficiency
                    self.delivOrder[self.i].sort()
        # Keep deliverying until orders exist alogn a vertical axis
                    while True:
                        if self.botCurrent[1] == self.delivOrder[self.i][0]:
        # Make a delivery , remove a delivered order from delivOrder dictionary
                            self.route.append('D')
                            self.delivOrder[self.i].pop(0)
                            if len(self.delivOrder[self.i]) > 0:

                                continue
                            else:
                                del self.delivOrder[self.i]

                                break
        # Decide which direction to move to the next order
                        elif self.botCurrent[1] < self.delivOrder[self.i][0]:
                            direction = 1
                            direction_ind = 'N'
                        else:
                            direction = -1
                            direction_ind = 'S'
        # Move to the next order location
                        while self.botCurrent[1] != self.delivOrder[self.i][0]:
                            self.botCurrent[1] += direction
                            self.route.append(direction_ind)

# Move pizzabot along a horizontal axis until all deliveries are done
        while self.delivOrder:

                for i in range(self.limits[0]):
                    if i in self.delivOrder:

                        deliverRow(i,self.botCurrent)
                        if len(self.delivOrder) == 0:
                            break

                    if self.delivOrder:
                        self.route.append('E')
                        self.botCurrent[0] = i

# Return a delivery route
    def __str__(self):
             return ''.join(self.route)

# Get the result route
    def getRoute(self):
             return ''.join(self.route)
