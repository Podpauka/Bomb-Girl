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


class Player:
    VELOCITY = 5

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self, direction: Direction):
        if direction == Direction.right:
            if self.x + PLAYER_WIDTH / 2 + self.VELOCITY <= SCREEN_WIDTH:
                self.x += self.VELOCITY
        elif direction == Direction.left:
            if self.x - PLAYER_WIDTH / 2 - self.VELOCITY >= 0:
                self.x -= self.VELOCITY
        elif direction == Direction.down:
            if self.y + PLAYER_HEIGHT / 2 + self.VELOCITY <= SCREEN_HEIGHT:
                self.y += self.VELOCITY
        elif direction == Direction.up:
            if self.y - PLAYER_HEIGHT / 2 - self.VELOCITY >= 0:
                self.y -= self.VELOCITY

    def display(self, screen):
        screen.blit(self.image, (self.x - PLAYER_WIDTH / 2, self.y - PLAYER_HEIGHT / 2))


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
    player = Player(16, 16, player_image)
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
