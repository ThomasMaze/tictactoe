from unittest import TestCase

from source.Grid import Grid

GRID_SIZE = 9


class GridTestCase(TestCase):

    def test_emptyGrid(self):
        grid = Grid()
        expectedGridRepresentation = [0] * GRID_SIZE
        self.assertTrue(grid.isEmpty(), "grid should be empty at creation")
        self.assertEqual(expectedGridRepresentation, grid.representation())

    def test_fillCell(self):
        grid = Grid()
        expectedGridRepresentation = [0,0,0,1,0,0,0,0,0]
        grid.fillCell(3)
        self.assertFalse(grid.isEmpty())
        self.assertEqual(expectedGridRepresentation, grid.representation())
