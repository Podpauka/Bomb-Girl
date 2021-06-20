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


class Direction(Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"


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


class Player:
    VELOCITY = 5

    def __init__(self, position: Vector, image):
        self.position = position
        self.image = image

    def move(self, direction: Direction):
        if direction == Direction.right:
            self.position.x += self.VELOCITY
        elif direction == Direction.left:
            self.position.x -= self.VELOCITY
        elif direction == Direction.down:
            self.position.y += self.VELOCITY
        elif direction == Direction.up:
            self.position.y -= self.VELOCITY

        self.position = self.position.clip_to_rect(
            left_top_corner=Vector(PLAYER_WIDTH / 2, PLAYER_HEIGHT / 2),
            right_bottom_corner=Vector(SCREEN_WIDTH - PLAYER_WIDTH / 2, SCREEN_HEIGHT - PLAYER_HEIGHT / 2)
        )

    def display(self, screen):
        screen.blit(self.image, (self.position.x - PLAYER_WIDTH / 2, self.position.y - PLAYER_HEIGHT / 2))


def main():
    pygame.init()
    background_color = (66, 227, 245)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("BomberGirl")
    clock = pygame.time.Clock()

    player_image = pygame.transform.scale2x(pygame.image.load("images\pf0.png"))
    # grass_image = pygame.transform.scale2x(pygame.image.load("images\grass.png"))

    movement = {pygame.K_UP: False, pygame.K_DOWN: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}
    running = True
    player = Player(Vector(PLAYER_WIDTH / 2, PLAYER_HEIGHT / 2), player_image)
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
        # screen.blit(grass_image, (50, 50))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()
