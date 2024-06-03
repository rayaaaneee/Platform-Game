from time import *


class useful:
    def __init__(self):
        self.tick = 0
        self.delta = 0
        self.lastTime = time()

    def tick(self):
        self.tick += 1

    def wait(self, time):
        while True:
            self.update()
            if self.delta >= time:
                break

    def update(self):
        self.delta = time() - self.lastTime
        self.lastTime = time()
