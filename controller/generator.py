import random
from model.field import Field


class Generator:
    @staticmethod
    def generate_field(width: int, height: int) -> Field:
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота поля должны быть положительными целыми числами.")

        field = Field(width, height)
        wall_probability = 0.3

        for y in range(height):
            for x in range(width):
                field.cells[y][x] = "wall" if random.random() < wall_probability else None

        return field
