import pygame
import os
from .taiko import Taiko
from .songselect import SongSelect


class Game:

    def __init__(self, song_path: str = "taiko_songs",
                 *, taiko: Taiko = None, select: SongSelect = None, x: int = 1280, y: int = 720, framerate: int = 144):
        self.x = x
        self.y = y
        self.framerate = framerate

        self.screen = None
        self.clock = None
        self.running = False
        self.game_loaded = False
        self.state = 0
        self.songs = []

        self.taiko = taiko if taiko else Taiko(self)
        self.song_select = select if select else SongSelect(self)

        if not os.path.exists(song_path):
            os.mkdir(song_path)

    def run(self):
        pygame.mixer.pre_init(44100)
        pygame.init()
        self.screen = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption("Taiko")
        self.clock = pygame.time.Clock()

        self.running = True

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if self.state == 0:
                    if event.type == pygame.KEYDOWN:
                        self.song_select.key_press(event.key)

            if not self.game_loaded and self.clock.get_fps() >= 1:
                self.game_loaded = True

            if self.game_loaded:
                if self.state == 0:
                    self.song_select.update()
                else:
                    self.taiko.update()
            self.clock.tick(self.framerate)
