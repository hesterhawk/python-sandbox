# Globals for the bearings
# Change the values as you see fit

# Wschod
EAST = 2

# Polnoc
NORTH = 1

# Zachod
WEST = 4

# Poludnie
SOUTH = 3

directions = {
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
    4: (-1, 0)
}

turns = {'R': 1, 'L': -1}

class Robot(object):

    bearing = NORTH
    coordinates = ()

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_right(self):
        self.bearing = 1 + self.bearing if 1 + self.bearing < 5 else 1
        return self.bearing

    def turn_left(self):
        self.bearing = self.bearing - 1 if self.bearing - 1 > 0 else 4
        return self.bearing

    def advance(self):
        result = map(lambda x,y: x+y,self.coordinates, directions[self.bearing])
        self.coordinates = tuple(list(result))

    def simulate(self, code):
        for turn in list(code):
            if 'R' == turn:
                self.turn_right()
            elif 'L' == turn:
                self.turn_left()
            else:
                self.advance()