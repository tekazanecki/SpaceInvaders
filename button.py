import pygame.font

class Button:
    """
    A class to represent a button in the game.
    """

    def __init__(self, game_settings, screen, msg):
        """
        Initialize button attributes.

        Args:
            game_settings: An instance of the settings class containing game settings.
            screen: The screen surface where the game is displayed.
            msg: The message to be displayed on the button.
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Define the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message elements
        self.msg_image = ''
        self.msg_image_rect = ''

        # Prepare the button message
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """
        Turn msg into a rendered image and center text on the button.

        Args:
            msg: The message to be displayed on the button.
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        Draw the button with color and then draw the text.
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
