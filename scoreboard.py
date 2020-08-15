import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # Font settings for scoring information.
        self.text_color_high = (238, 99, 99)
        self.text_color_level = (255, 185, 15)
        self.text_color_score = (0, 205, 205)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_level()
        self.prep_high_score()
        self.prep_ships()

    def prep_score(self):  # 展示分数
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))  # 参数-1表示取整到十位数,-2表示取整到百位数
        score_str = "{:,}".format(rounded_score)  # 字符格式化
        score_str = "Score " + score_str
        self.score_image = self.font.render(score_str, True, self.text_color_score,
            self.ai_settings.bg_color)
            
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):  # 展示当前等级
        """Turn the level into a rendered image."""
        self.level_image = self.font.render("Level " + str(self.stats.level), True,
                                            self.text_color_level, self.ai_settings.bg_color)

        # Position the level left to the score for 120.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.left - 120
        self.level_rect.top = self.score_rect.top

    def prep_high_score(self):  # 展示最高分
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        high_score_str = "High " + high_score_str
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color_high, self.ai_settings.bg_color)
                
        # Position the high score left to the level for 120.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.level_rect.left - 120
        self.high_score_rect.top = self.score_rect.top

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)  # 添加到编组中
        
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)  # 显示当前得分
        self.screen.blit(self.high_score_image, self.high_score_rect)  # 显示最高得分
        self.screen.blit(self.level_image, self.level_rect)  # 显示等级
        # Draw ships.
        self.ships.draw(self.screen)
