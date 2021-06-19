import sys
import pygame


# 1. rysowanie, okno, mapa, grafika
# 2. poruszanie się
# 3. kolizje
# 4. gracz
# 5. przeciwnik


def main():
    pygame.init()
    background_color = (66, 227, 245)
    screen = pygame.display.set_mode((1025, 768))
    pygame.display.set_caption("BomberGirl")
    clock = pygame.time.Clock()

    player = pygame.image.load("images\pf0.png")
    player_x = 0
    player_y = 0

    movement = {pygame.K_UP: False, pygame.K_DOWN: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}
    running = True
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
            if player_x <= 1000:
                player_x += 4
        elif movement[pygame.K_DOWN]:
            if player_y <= 760:
                player_y += 4
        elif movement[pygame.K_LEFT]:
            if player_x >= 0.5:
                player_x -= 4
        elif movement[pygame.K_UP]:
            if player_y >= 0.5:
                player_y -= 4
        screen.blit(player, (player_x, player_y))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()
