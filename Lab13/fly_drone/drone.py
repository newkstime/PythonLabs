class Drone:
    def __init__(self):
        self.drone_speed = 0.0
        self.drone_height = 0.0

    def accelerate(self):
        self.drone_speed += 10

    def decelerate(self):
        self.drone_speed -= 10
        if self.drone_speed < 0:
            self.drone_speed = 0

    def ascend(self):
        self.drone_height += 10

    def descend(self):
        self.drone_height -= 10
        if self.drone_height < 0:
            self.drone_height = 0


