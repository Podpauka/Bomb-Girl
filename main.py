import sys
import pygame

# 1. rysowanie, okno, mapa, grafika
# 2. poruszanie się
# 3. kolizje
# 4. gracz
# 5. przeciwnik


# class Position:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


class Player:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move_right(self):
        if self.x <= 990:
            self.x += 4

    def move_left(self):
        if self.x >= 0.5:
            self.x -= 4

    def move_down(self):
        if self.y <= 735:
            self.y += 4

    def move_up(self):
        if self.y >= 0.5:
            self.y -= 4

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

def main():
    pygame.init()
    background_color = (66, 227, 245)
    screen = pygame.display.set_mode((1025, 768))
    pygame.display.set_caption("BomberGirl")
    clock = pygame.time.Clock()

    player_image = pygame.transform.scale2x(pygame.image.load("images\pf0.png"))
    # grass_image = pygame.transform.scale2x(pygame.image.load("images\grass.png"))

    movement = {pygame.K_UP: False, pygame.K_DOWN: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}
    running = True
    player = Player(0, 0, player_image)
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
            player.move_right()
        elif movement[pygame.K_DOWN]:
            player.move_down()
        elif movement[pygame.K_LEFT]:
            player.move_left()
        elif movement[pygame.K_UP]:
            player.move_up()
        player.display(screen)
        # screen.blit(grass_image, (50, 50))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()
