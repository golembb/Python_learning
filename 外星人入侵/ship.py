import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):  # screen指定将飞船绘制在什么地方
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings  # 让飞船能够获取速度设置
        self.image = pygame.image.load('images/ship_3.bmp')  # 下载图片
        self.rect = self.image.get_rect()  # 获取pygame中get_rect()的属性
        self.screen_rect = screen.get_rect()  # 将屏幕存储
        self.rect.centerx = self.screen_rect.centerx  # 让飞船的坐标等于屏幕xy的坐标
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)  # rect只能存储整数部分，因此需要一个新属性
        self.moving_right = False  # 飞船移动标志
        self.moving_left = False

    def update(self):  # 根据移动标志调整移动位置
        if self.moving_right and self.rect.right < self.screen_rect.right:  # 飞船的边界值小于屏幕的边界值就运行
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:  # 如果使用elif的话，上一个if会永远处于优先位置
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx  # 将center属性设置为屏幕中心的x坐标

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # 根据self.rect的位置将图形绘制
