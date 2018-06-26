class Drone:
    def __init__(self):
        self.__drone_speed = 0.0
        self.__drone_height = 0.0

    def accelerate(self):
        self.__drone_speed += 10

    def decelerate(self):
        self.__drone_speed -= 10
        if self.__drone_speed < 0:
            self.__drone_speed = 0

    def ascend(self):
        self.__drone_height += 10

    def descend(self):
        self.__drone_height -= 10
        if self.__drone_height < 0:
            self.__drone_height = 0

    def __str__(self):
        return "Speed: " + str(self.__drone_speed) + " Height: " + str(self.__drone_height)


