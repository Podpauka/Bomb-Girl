import json
import sys
import pygame
from enum import Enum

# 1. rysowanie, okno, mapa, grafika
# 2. poruszanie się
# 3. kolizje
# 4. gracz
# 5. przeciwnik


PLAYER_WIDTH = 32
PLAYER_HEIGHT = 32
SCREEN_WIDTH = 1025
SCREEN_HEIGHT = 768
WALL_WIDTH = 32
WALL_HEIGHT = 32


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        new_vector = Vector(x, y)
        return new_vector

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        new_vector = Vector(x, y)
        return new_vector

    def clip_to_rect(self, left_top_corner: "Vector", right_bottom_corner: "Vector") -> "Vector":
        new_vector_x = self.x
        new_vector_y = self.y
        if new_vector_x < left_top_corner.x:
            new_vector_x = left_top_corner.x
        elif new_vector_x > right_bottom_corner.x:
            new_vector_x = right_bottom_corner.x
        if new_vector_y < left_top_corner.y:
            new_vector_y = left_top_corner.y
        elif new_vector_y > right_bottom_corner.y:
            new_vector_y = right_bottom_corner.y
        return Vector(new_vector_x, new_vector_y)


class Wall:
    def __init__(self, position: Vector, image: pygame.Surface):
        self.position = position
        self.image = image

    def display(self, screen: pygame.Surface):
        screen.blit(self.image, (self.position.x - WALL_WIDTH / 2, self.position.y - WALL_HEIGHT / 2))


class Direction(Enum):
    up = Vector(0, -1)
    down = Vector(0, 1)
    left = Vector(-1, 0)
    right = Vector(1, 0)


class Player:
    VELOCITY = 5

    def __init__(self, position: Vector, image: pygame.Surface):
        self.position = position
        self.image = image

    def move(self, direction: Direction):
        self.position = self.position + (direction.value * self.VELOCITY)
        self.position = self.position.clip_to_rect(
            left_top_corner=Vector(PLAYER_WIDTH / 2, PLAYER_HEIGHT / 2),
            right_bottom_corner=Vector(SCREEN_WIDTH - PLAYER_WIDTH / 2, SCREEN_HEIGHT - PLAYER_HEIGHT / 2)
        )

    def display(self, screen: pygame.Surface):
        screen.blit(self.image, (self.position.x - PLAYER_WIDTH / 2, self.position.y - PLAYER_HEIGHT / 2))


def main():
    pygame.init()
    background_color = (0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("BomberGirl")
    clock = pygame.time.Clock()

    player_image = pygame.transform.scale2x(pygame.image.load("images\pf0.png"))
    wall_image = pygame.transform.scale2x(pygame.image.load("images\\block.png"))
    # grass_image = pygame.transform.scale2x(pygame.image.load("images\grass.png"))

    movement = {pygame.K_UP: False, pygame.K_DOWN: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}
    running = True
    player = Player(Vector(PLAYER_WIDTH / 2, PLAYER_HEIGHT / 2), player_image)
    with open("map1.json") as file_map:
        bomber_map = json.load(file_map)
    walls = [Wall(Vector(x, y), wall_image) for x, y in bomber_map["walls"]]

    while running:
        screen.fill(background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                movement[event.key] = True
            elif event.type == pygame.KEYUP:
                movement[event.key] = False
        if movement[pygame.K_RIGHT]:
            player.move(Direction.right)
        elif movement[pygame.K_DOWN]:
            player.move(Direction.down)
        elif movement[pygame.K_LEFT]:
            player.move(Direction.left)
        elif movement[pygame.K_UP]:
            player.move(Direction.up)
        player.display(screen)
        for wall in walls:
            wall.display(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()
