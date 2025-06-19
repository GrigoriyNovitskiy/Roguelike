import unittest
from unittest.mock import Mock, patch
import pygame
from model.game import Game
from controller.game_controller import GameController


class TestGameController(unittest.TestCase):

    def setUp(self):
        self.game_controller = GameController()

    @patch('controller.game_controller.Game')
    def test_initialization(self, MockGame):
        mock_game_instance = MockGame.return_value
        game_controller = GameController()
        self.assertEqual(game_controller.game, mock_game_instance)

    def test_handle_event_up(self):
        self.game_controller.game.move_player = Mock()
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_w)
        self.game_controller.handle_event(event)
        self.game_controller.game.move_player.assert_called_once_with("up")

    def test_handle_event_down(self):
        self.game_controller.game.move_player = Mock()
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_s)
        self.game_controller.handle_event(event)
        self.game_controller.game.move_player.assert_called_once_with("down")

    def test_handle_event_left(self):
        self.game_controller.game.move_player = Mock()
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a)
        self.game_controller.handle_event(event)
        self.game_controller.game.move_player.assert_called_once_with("left")
        
    def test_handle_event_invalid_key(self):
        self.game_controller.game.move_player = Mock()
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_z)
        self.game_controller.handle_event(event)
        self.game_controller.game.move_player.assert_not_called()

    def test_handle_event_right(self):
        self.game_controller.game.move_player = Mock()
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d)
        self.game_controller.handle_event(event)
        self.game_controller.game.move_player.assert_called_once_with("right")

    def test_update(self):
        self.game_controller.game.update = Mock()
        self.game_controller.update()
        self.game_controller.game.update.assert_called_once()

    def test_get_game_state(self):
        self.game_controller.game.get_state = Mock(return_value="game_state")
        state = self.game_controller.get_game_state()
        self.assertEqual(state, "game_state")
        self.game_controller.game.get_state.assert_called_once()
    def test_handle_event_non_keydown(self):
        self.game_controller.game.move_player = Mock()
        event = pygame.event.Event(pygame.KEYUP, key=pygame.K_w)
        self.game_controller.handle_event(event)
        self.game_controller.game.move_player.assert_not_called()

    def test_handle_event_none(self):
        self.game_controller.game.move_player = Mock()
        with self.assertRaises(AttributeError):
            self.game_controller.handle_event(None)

    def test_handle_event_missing_key_attr(self):
        class DummyEvent:
            type = pygame.KEYDOWN
        dummy_event = DummyEvent()
        self.game_controller.game.move_player = Mock()

        with self.assertRaises(AttributeError):
            self.game_controller.handle_event(dummy_event)


if __name__ == '__main__':
    unittest.main()