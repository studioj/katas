title = "mars_rover"


class Rover(object):
    def __init__(self, direction, x, y):
        self.__x = x
        self.__y = y
        self.location = (self.__x, self.__y)

    def forward(self):
        self.__y += 1
        self.location = (self.__x, self.__y)
