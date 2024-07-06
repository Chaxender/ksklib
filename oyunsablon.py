import pygame
import random

# Pygame başlatma
pygame.init()

# Oyun alanı ve diğer değişkenler
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basit Oyun")

# Oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ekranı temizleme ve güncelleme
    screen.fill((255, 255, 255))
    pygame.display.flip()

# Pygame kapatma
pygame.quit()
