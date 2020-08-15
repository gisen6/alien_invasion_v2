import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen. 飞船的初始位置
        self.rect.centerx = self.screen_rect.centerx  # 飞船图像矩形的中心的x坐标设置为屏幕矩形的中心x坐标
        self.rect.bottom = self.screen_rect.bottom  # 飞船图像矩形的下边缘的y坐标设置为屏幕矩形的下边缘y坐标

        # Store a decimal value for the ship's center.
        self.center_x = float(self.rect.centerx)  # x坐标支持小数的增量移动
        self.center_y = float(self.rect.centery)  # y坐标支持小数的增量移动
        
        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False  # 支持向上移动
        self.moving_down = False  # 支持向下移动
        
    def center_ship(self):  # 飞船位置回到页面底部中间
        """Center the ship on the screen."""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center_x = float(self.rect.centerx)  # 重新初始化center_x的值
        self.center_y = float(self.rect.centery)  # 重新初始化center_y的值

        
    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:  # 向上移动
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:  # 向下移动
            self.center_y += self.ai_settings.ship_speed_factor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y  # 飞船的y坐标

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
