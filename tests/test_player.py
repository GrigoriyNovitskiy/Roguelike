import unittest
from model.position import Position
from model.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_initial_position(self):
        self.assertEqual(self.player.position.x, 0)
        self.assertEqual(self.player.position.y, 0)

    def test_move_up(self):
        self.player.move("up", None)
        self.assertEqual(self.player.position.x, 0)
        self.assertEqual(self.player.position.y, -1)

    def test_invalid_direction(self):
        original_position = (self.player.position.x, self.player.position.y)
        self.player.move("diagonal", None)
        self.assertEqual((self.player.position.x, self.player.position.y), original_position)

    def test_none_direction(self):
        original_position = (self.player.position.x, self.player.position.y)
        self.player.move(None, None)
        self.assertEqual((self.player.position.x, self.player.position.y), original_position)

    def test_custom_start_position(self):
        self.player.position = Position(5, 5)
        self.player.move("left", None)
        self.assertEqual(self.player.position.x, 4)
        self.assertEqual(self.player.position.y, 5)

    def test_multiple_moves(self):
        self.player.move("right", None)
        self.player.move("down", None)
        self.player.move("down", None)
        self.assertEqual(self.player.position.x, 1)
        self.assertEqual(self.player.position.y, 2)


    def test_move_down(self):
        self.player.move("down", None)
        self.assertEqual(self.player.position.x, 0)
        self.assertEqual(self.player.position.y, 1)

    def test_move_left(self):
        self.player.move("left", None)
        self.assertEqual(self.player.position.x, -1)
        self.assertEqual(self.player.position.y, 0)

    def test_move_right(self):
        self.player.move("right", None)
        self.assertEqual(self.player.position.x, 1)
        self.assertEqual(self.player.position.y, 0)


if __name__ == '__main__':
    unittest.main()