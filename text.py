import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("نمایش متن")
clock  = pygame.time.Clock()

# ── ساخت فونت ──────────────────────────────────────
# روش ۱: فونت پیش‌فرض سیستم
font_big    = pygame.font.SysFont('Arial', 64)
font_medium = pygame.font.SysFont('Arial', 36)
font_small  = pygame.font.SysFont('Arial', 24)

BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
YELLOW = (255, 220, 0)
RED    = (255, 80, 80)
CYAN   = (0, 255, 255)

score  = 0
timer  = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score += 10

    timer += 1

    # ── رندر ──────────────────────────────────────
    screen.fill(BLACK)

    # render(متن, anti-alias, رنگ)
    title_surf  = font_big.render(" Game ", True, YELLOW)
    score_surf  = font_medium.render(f"score: {score}", True, WHITE)
    timer_surf  = font_medium.render(f"frame: {timer}", True, CYAN)
    hint_surf   = font_small.render("Space = +10 point", True, RED)

    # blit — قرار دادن روی صفحه (surface, (x, y))
    screen.blit(title_surf,  (250, 80))
    screen.blit(score_surf,  (300, 220))
    screen.blit(timer_surf,  (300, 300))
    screen.blit(hint_surf,   (270, 520))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
