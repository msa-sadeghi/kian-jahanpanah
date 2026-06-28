import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎨 بازی رنگ‌ها")
clock = pygame.time.Clock()

# رنگ‌های آماده
COLORS = [
    (255, 0,   0  ),   # قرمز
    (0,   255, 0  ),   # سبز
    (0,   0,   255),   # آبی
    (255, 255, 0  ),   # زرد
    (255, 0,   255),   # صورتی
    (0,   255, 255),   # فیروزه‌ای
    (255, 165, 0  ),   # نارنجی
    (128, 0,   128),   # بنفش
]

current_color = (30, 30, 30)   # رنگ اولیه
color_index   = 0

running = True
while running:

    # ── رویدادها ──────────────────────────────────
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # با هر کلیک ماوس رنگ عوض می‌شود
        if event.type == pygame.MOUSEBUTTONDOWN:
            color_index = (color_index + 1) % len(COLORS)
            current_color = COLORS[color_index]

        # با Space رنگ تصادفی
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )

    # ── رندر ──────────────────────────────────────
    screen.fill(current_color)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
