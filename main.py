import PIL.Image
import math

class Sheet:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.tableau = []
        self.__createTableau(color)
        self.image = None

    def __createTableau(self, color):
        self.tableau = [[color for i in range(self.x)] for j in range(self.y)]

    def createImage(self):
        self.image = PIL.Image.new(mode="RGB", size=(self.x, self.y))
        for x in range(self.x):
            for y in range(self.y):
                self.image.putpixel((x, y), self.tableau[x][y])

    def showImage(self):
        self.image.show()

class Geometry(Sheet):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def isLyingWithinCircle(self, radius, centre=[], point=[]):
            return True if self.distanceFromCircle(centre, point) < radius else False

    def isPointOnCircle(self, radius, centre=[], point=[]):
        return pow(radius, 2) == pow(point[0] - centre[0], 2) + pow((point[1] - centre[1]), 2)

    def createCircle(self, radius, centre=[], color=()):
        for x in range(self.x):
            for y in range(self.y):
                try:
                    if self.isPointOnCircle(radius, centre, [x, y]) or self.isLyingWithinCircle(radius, centre, [x, y]):
                        self.tableau[x][y] = color
                except:
                    pass

    def distanceFromCircle(self, centre=[], point=[]):
            return math.sqrt(math.pow(point[0] - centre[0], 2) + math.pow((point[1] - centre[1]), 2))


    def applyGradient(self):
        pass

if __name__ == '__main__':
    geo = Geometry(1000, 1000, (200, 200, 200))
    geo.createCircle(200, [800, 700], (255, 255, 0)) #yellow
    geo.createCircle(300, [500, 500], (0, 0, 255)) #blue
    geo.createCircle(550, [100, 100], (255, 0, 0)) #red
    geo.createImage()
    geo.showImage()





