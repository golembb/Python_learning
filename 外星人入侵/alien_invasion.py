import pygame
from pygame.sprite import Group
from settings import Setting
from game_stas import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()  # 初始化背景设置
    a_setting = Setting()
    pygame.time.set_timer(a_setting.fire_event, 250)
    screen = pygame.display.set_mode(size=(a_setting.screen_width, a_setting.screen_height))  # 指定游戏窗口尺寸
    pygame.display.set_caption('外星人入侵')
    play_button = Button(a_setting,screen, 'Play')
    stats = GameStats(a_setting)
    sb = Scoreboard(a_setting, screen, stats)
    # bg_color = (230, 230 , 230) 设置背景色,运用Settings类后就不用提前设置了
    ship = Ship(a_setting, screen)
    bullets = Group()
    aliens = Group()  # 空编组储存所有外星人
    gf.create_fleet(a_setting, screen, ship, aliens)  # 创建外星人群

    while True:
        gf.check_events(a_setting, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(a_setting, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(a_setting, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(a_setting, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
