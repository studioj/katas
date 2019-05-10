title = "mars_rover"


class Rover(object):
    def __init__(self, direction):
        self.__x = 0
        self.__y = 0
        self.direction = direction
        self.location = (self.__x, self.__y)

    def forward(self):
        north_south = {"N": 1, "S": -1}
        east_west = {"E": 1, "W": -1}
        if self.direction in north_south.keys():
            self.__y += north_south[self.direction]
        elif self.direction in east_west.keys():
            self.__x += east_west[self.direction]
        self.location = (self.__x, self.__y)
