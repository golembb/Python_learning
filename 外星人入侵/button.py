import pygame.font  # 将文本渲染到屏幕上


class Button:
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()  # 创建一个表示屏幕的属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)  # none表示使用默认字体，第二个参数表示字体大小
        self.rect = pygame.Rect(0, 0, self.width, self.height)  # 创建一个表示按钮的rect属性
        self.rect.center = self.screen_rect.center  # 将屏幕居中的属性传给按钮
        self.prep_msg(msg)

    def prep_msg(self, msg):  # 将msg渲染成图像，并使其按钮居中
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)  # 将文本转换为图像，True表示开启反锯齿功能
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center  # 让文本图像在按钮上居中

    def draw_button(self):  # 让按钮显示到屏幕上
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)














