import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    def __init__(self, ai_settings, screen, stats):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (30, 30, 30)  # 字体颜色
        self.font = pygame.font.SysFont(None, 36)
        self.prep_score()  # 将得分转化为图像
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        score_str = "{:,}".format(self.stats.score)  # 在字符串中插入逗号
        self.score_image = self.font.render('score: ' + score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # 设置得分的位置
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render('high score: ' + high_score_str, True, self.text_color,
                                                 self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        self.level_image = self.font.render('level: ' + str(self.stats.level), True, self.text_color,
                                            self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        self.ships = Group()  # 创建一个用于存储飞船的空编组
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width  # 每艘飞船间距10
            ship.rect.y = 10
            self.ships.add(ship)  # 将新飞船都添加到编组中

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)  # 对编组调用draw，在屏幕上显示飞船





























