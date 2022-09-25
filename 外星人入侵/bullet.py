import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # 继承Sprite类，给相关元素编组
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)  # 创建子弹的属性，子弹并非是基于图像，因此要用rect从空白处创建
        self.rect.centerx = ship.rect.centerx  # 将飞船的坐标基于子弹
        self.rect.top = ship.rect.top  # 子弹从飞船顶部射出
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):  # 向上移动子弹
        self.y -= self.speed_factor  # 原点位置位于屏幕左上角，因此子弹不断上升的话坐标要相应缩小
        self.rect.y = self.y  # x坐标始终没变，因此子弹发出后一直向上

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)  # 在屏幕上绘制子弹
