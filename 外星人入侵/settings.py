import pygame


class Setting:  # 存出“外星人入侵“所有设置的类
    def __init__(self):
        self.screen_width = 1500
        self.screen_height = 790
        self.bg_color = (238, 244, 251)
        self.ship_limit = 2
        self.bullet_width = 3  # 子弹设置
        self.bullet_height = 15
        self.bullet_color = 150, 60, 60
        self.bullet_allowed = 7  # 屏幕上允许出现的子弹数量
        self.fleet_drop_speed = 10  # 下降速度
        self.speedup_scale = 1.1  # 游戏节奏的加快速度
        self.score_scale = 10  # 得分提高速度
        self.initialize_dynamic_settings()  # 初始化随游戏进行而变化的属性
        self.fire_event = pygame.USEREVENT

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1  # 因为外星人只往左右两个方向移动，因此确定方位然后加1减1更好
        self.alien_points = 20  # 击落一架外星人的得分

    def increase_speed(self):
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points + self.score_scale)





