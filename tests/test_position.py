import unittest
from model.position import Position


class TestPosition(unittest.TestCase):

    def test_initialization(self):
        pos = Position(0, 0)
        self.assertEqual(pos.x, 0)
        self.assertEqual(pos.y, 0)

        pos = Position(10, -5)
        self.assertEqual(pos.x, 10)
        self.assertEqual(pos.y, -5)

    def test_move_zero(self):
        pos = Position(1, 1)
        pos.move(0, 0)
        self.assertEqual(pos.x, 1)
        self.assertEqual(pos.y, 1)

    def test_negative_position(self):
        pos = Position(-10, -10)
        pos.move(-5, -5)
        self.assertEqual(pos.x, -15)
        self.assertEqual(pos.y, -15)

    def test_large_position(self):
        pos = Position(1_000_000, 1_000_000)
        pos.move(1_000_000, -500_000)
        self.assertEqual(pos.x, 2_000_000)
        self.assertEqual(pos.y, 500_000)

    def test_move_from_zero(self):
        pos = Position(0, 0)
        pos.move(-1, 1)
        self.assertEqual(pos.x, -1)
        self.assertEqual(pos.y, 1)

    def test_move_with_float(self):
        pos = Position(0, 0)
        pos.move(1.5, -2.3)
        self.assertEqual(pos.x, 1.5)
        self.assertEqual(pos.y, -2.3)

    def test_move(self):
        pos = Position(0, 0)
        pos.move(5, -3)
        self.assertEqual(pos.x, 5)
        self.assertEqual(pos.y, -3)

        pos.move(-2, 2)
        self.assertEqual(pos.x, 3)
        self.assertEqual(pos.y, -1)

if __name__ == '__main__':
    unittest.main()