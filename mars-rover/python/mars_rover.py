title = "mars_rover"


class Rover(object):
    def __init__(self, direction):
        self.__x = 0
        self.__y = 0
        self.location = (self.__x, self.__y)

    def forward(self):
        self.__y += 1
        self.location = (self.__x, self.__y)
