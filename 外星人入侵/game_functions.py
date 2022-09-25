import sys  # 用此模块推出游戏
from time import sleep  # 让游戏暂停
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets):  # 函数分离，为了使check_event更简单
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        create_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:  # 可按esc退出游戏
        stats.save_high_score()
        sys.exit()
    elif event.key == pygame.K_TAB:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False  # 跳转到ship中的update函数
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):  # 响应按键与鼠标的事件,形参位置都不能乱
    for event in pygame.event.get():  # 为了让程序源源不断的响应用户事件
        if event.type == pygame.QUIT:  # 单击游戏窗口关闭按钮退出游戏
            stats.save_high_score()  # 保存最高分
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # 返回一个元组，其中包含玩家单点鼠标的x和y做表
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    pygame.mouse.set_visible(False)  # 让光标不可见
    stats.reset_stats()
    stats.game_active = True  # 设为True，这样代码运行完游戏就会开始
    sb.prep_score()
    sb.prep_level()
    sb.prep_ship()
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)  # 检查鼠标单击位置是否在play按键的rect内
    if button_clicked and not stats.game_active:  # 仅当玩家单击了play按钮且游戏处于非活跃状态时游戏才会重新开始
        ai_settings.initialize_dynamic_settings()  # 重置所有速度
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width  # 计算可放置外星人的空间，减去了两个外星人宽度的边距
    number_alien_x = int(available_space_x / (2 * alien_width))  # 考虑到外星人之间的间距，用可放空间除以两个外星人的宽度
    return number_alien_x


def get_number_rows(ai_settings, ship_height, alien_height):  # 计算屏幕可容纳多少行外星人
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)  # 在创建前需要知道外星人的宽度与高度，因此先独立创建一个外星人
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):  # 从零数到要创建的外星人行数
        for alien_number in range(number_aliens_x):  # 从零数到要创建的外星人数
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def create_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:  # 屏幕上的子弹数小于允许数时才会创建新子弹
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    cllisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 检查是否有子弹击中外星人，如果击中就删除相应外星人与子弹
    if cllisions:
        for aliens in cllisions.values():
            stats.score += ai_settings.alien_points * len(aliens)  # 遍历字典中所有的值，将得分乘以个数就不会遗漏一次性杀掉的外星人了
            sb.prep_score()  # 将更新得分的图像创建出来
        check_high_score(stats, sb)
    if len(aliens) == 0:  # 检查外星人是否为空，然后创建一群新的外星人
        bullets.empty()  # 清除所有子弹
        ai_settings.increase_speed()  # 每过一关提升速度
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():  # 将到达顶端的子弹删除
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1  # 下降后往相反的方向移动


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1  # 将飞船减一
        sb.prep_ship()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens, )  # 创建新的外星人
        ship.center_ship()  # 把飞船放在中间
        sleep(0.5)  # 暂停0.5秒
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):  # 对编组中所有的外星人都调用update
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):  # spritecollideany检查编组与成员是否发生碰撞，发生后停止遍历编组
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):  # 更新屏幕图像
    screen.fill(ai_settings.bg_color)  # 每次循环时都重绘屏幕
    for bullet in bullets.sprites():  # 返回一个子弹编组
        bullet.draw_bullet()
    ship.blitme()  # 将飞船绘制在屏幕上
    aliens.draw(screen)  # 对编组使用draw，pymage会自动绘制编组的每个元素
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()  # 每次while循环会创建一个空屏幕，擦去旧屏幕，营造平滑移动的效果
