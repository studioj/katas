title = "mars_rover"


class Rover(object):
    def __init__(self, direction, x, y):
        self.location = (x, y)

    def forward(self):
        self.location = (0, 1)
