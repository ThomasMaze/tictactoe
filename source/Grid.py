

class Grid(object):

    GRID_SIZE = 9

    cells = [0]*GRID_SIZE

    def isEmpty(self):
        return self.cells.count(1) == 0

    def fillCell(self, cellId):
        self.cells[cellId] = 1

    def representation(self):
        return self.cells

