import pygame
import sys
import random
import asyncio

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cupcake Collector")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 28, bold=True)
big_font = pygame.font.SysFont("arial", 56, bold=True)

async def main():
    player_img = pygame.image.load("assets/player.png").convert_alpha()
    cupcake_img = pygame.image.load("assets/cupcake.png").convert_alpha()
    jump_snd = pygame.mixer.Sound("assets/jump.ogg")
    collect_snd = pygame.mixer.Sound("assets/collect.ogg")
    win_snd = pygame.mixer.Sound("assets/win.ogg")

    player = pygame.Rect(380, 100, 40, 40)
    vel_x = 0
    vel_y = 0
    speed = 6
    gravity = 0.8
    jump_strength = -15
    is_grounded = False

    platforms = [
        pygame.Rect(0, 550, 800, 50),
        pygame.Rect(80, 420, 220, 20),
        pygame.Rect(340, 320, 200, 20),
        pygame.Rect(560, 220, 180, 20),
        pygame.Rect(180, 180, 160, 20)
    ]

    def reset_game():
        nonlocal player, vel_x, vel_y, is_grounded
        player.x, player.y = 380, 100
        vel_x, vel_y = 0, 0
        is_grounded = False
        items = []
        for _ in range(10):
            rx = random.randint(60, 740)
            ry = random.randint(60, 490)
            items.append(pygame.Rect(rx, ry, 28, 28))
        return items

    cupcakes = reset_game()
    total_cupcakes = 10
    won = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and won and event.key == pygame.K_r:
                cupcakes = reset_game()
                won = False

        keys = pygame.key.get_pressed()
        vel_x = 0
        if keys[pygame.K_LEFT]:
            vel_x = -speed
        if keys[pygame.K_RIGHT]:
            vel_x = speed
        if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and is_grounded:
            vel_y = jump_strength
            is_grounded = False
            jump_snd.play()

        vel_y += gravity
        player.x += vel_x
        if player.left < 0:
            player.left = 0
        if player.right > WIDTH:
            player.right = WIDTH

        player.y += vel_y
        is_grounded = False

        for p in platforms:
            if player.colliderect(p):
                if vel_y > 0 and player.bottom - vel_y <= p.top + 6:
                    player.bottom = p.top
                    vel_y = 0
                    is_grounded = True
                elif vel_y < 0 and player.top - vel_y >= p.bottom - 6:
                    player.top = p.bottom
                    vel_y = 0

        if player.bottom > 550:
            player.bottom = 550
            vel_y = 0
            is_grounded = True

        for c in cupcakes[:]:
            if player.colliderect(c):
                cupcakes.remove(c)
                collect_snd.play()
                if len(cupcakes) == 0 and not won:
                    won = True
                    win_snd.play()

        screen.fill((25, 25, 35))

        for p in platforms:
            pygame.draw.rect(screen, (70, 130, 240), p, border_radius=6)
            pygame.draw.rect(screen, (100, 160, 255), p, 2, border_radius=6)

        for c in cupcakes:
            screen.blit(cupcake_img, c)

        screen.blit(player_img, player)

        score_text = font.render(f"Cupcakes Left: {len(cupcakes)}/{total_cupcakes}", True, (255, 235, 120))
        screen.blit(score_text, (20, 20))

        if won:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            screen.blit(overlay, (0, 0))
            win_msg = big_font.render("ALL CUPCAKES COLLECTED!", True, (255, 215, 0))
            sub_msg = font.render("Press 'R' to Play Again", True, (255, 255, 255))
            screen.blit(win_msg, win_msg.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
            screen.blit(sub_msg, sub_msg.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()

asyncio.run(main())
