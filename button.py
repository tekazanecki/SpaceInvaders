import pygame.font

class Button():

    def __init__(self, game_settings, screen, msg):
        """Inicjalizacja atrybutów przycisku"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # zdefiniowanie wymiarów i właściwości przycisku
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.tex_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # utworzenie prostokąta
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # elementy wiadomości
        self.msg_image = ''
        self.msg_image_rect = ''

        # komunikat wyświetlany przez przycisk trzeba przygotować tylko jednokrotnie
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Umieszczenie tekstu w wygenerowanym obrazie"""
        self.msg_image = self.font.render(msg, True, self.tex_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Wyświetlenie pustego przycisku, a następnie komunikatu na nim"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)