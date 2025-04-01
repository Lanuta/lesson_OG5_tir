import pygame
import random
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/apple.png")
target_rect = target_img.get_rect()  # Получаем прямоугольник изображения
target_rect.x = random.randint(0, SCREEN_WIDTH - target_rect.width)
target_rect.y = random.randint(0, SCREEN_HEIGHT - target_rect.height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running = True
while running:
        screen.fill(color)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                        if target_rect.collidepoint(event.pos):  # Проверяем, попал ли клик в цель
                                target_rect.x = random.randint(0, SCREEN_WIDTH - target_rect.width)
                                target_rect.y = random.randint(0, SCREEN_HEIGHT - target_rect.height)

        screen.blit(target_img, (target_rect.topleft))
        pygame.display.update()

pygame.quit()