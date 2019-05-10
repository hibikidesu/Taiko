import pygame


class Taiko:

    def __init__(self, game):
        self.game = game
        self.ms = 0
        self.__hit = [round(self.game.x / 4), round(self.game.y / 2)]

    def update(self):
        self.ms += round(1000 / self.game.clock.get_fps())

        self.game.screen.fill((255, 255, 255))

        pygame.draw.circle(self.game.screen, (0, 0, 0), self.__hit, 50, 0)

        pygame.display.flip()
