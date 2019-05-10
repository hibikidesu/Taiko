import pygame


class SongSelect:

    def __init__(self, game):
        self.game = game
        self.ms = 0

        self.curr_song = 0

    def key_press(self, key):
        if key not in [276, 275]:
            return
        self.curr_song += 1 if key == 276 else -1
        if self.curr_song <= -1:
            self.curr_song = len(self.game.songs) - 1
        elif self.curr_song > len(self.game.songs) - 1:
            self.curr_song = 0

    def update(self):
        self.ms += round(1000 / self.game.clock.get_fps())
        self.game.screen.fill((255, 255, 255))

        pygame.display.flip()
