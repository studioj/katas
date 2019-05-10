title = "mars_rover"


class Rover(object):
    def __init__(self, direction):
        self.__x = 0
        self.__y = 0
        self.direction = direction
        self.location = (self.__x, self.__y)

    def forward(self):
        if self.direction == "N":
            self.__y += 1
        elif self.direction == "S":
            self.__y -= 1
        elif self.direction == "E":
            self.__x += 1
        self.location = (self.__x, self.__y)
