import json

class GameSaver:
    @staticmethod
    def save_game(game_state, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(game_state, file, indent=4)
        except (IOError, TypeError) as e:
            raise RuntimeError(f"Ошибка при сохранении игры: {e}")
