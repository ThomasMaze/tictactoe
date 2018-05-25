

class Grid(object):

    GRID_SIZE = 9

    empty = True
    cells = [0]*GRID_SIZE

    def isEmpty(self):
        return self.empty

    def fillCell(self, cellId):
        self.cells[cellId] = 1
        self.empty = False

    def representation(self):
        return self.cells

