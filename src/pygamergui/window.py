# importing needed modules
from rich.console import Console
import pygame

cons = Console()


# ------------------------------

# ------app class------
class app():
    """it`s the main window on which you will create your gui"""

    def __init__(self, w=600, h=600, target=None, bgcolor=(0, 0, 0), title="pygamegui", update_rate=7, background = None):
        self.w = w
        self.h = h

        self.target = target
        self.title = title

        self.bgcolor = bgcolor
        self.scren = pygame.display.set_mode((self.w, self.h))

        self.colock = pygame.time.Clock()
        self.eve = None
        self.fps = update_rate

        self.background = background

    def run(self):
        pygame.display.set_caption(self.title)
        cons.print("[green]sucessfully ran the app[/green]")
        try:
            if self.background is not None:
                bgimg = pygame.image.load(f'{self.background}')
        except Exception :
            raise Exception(f"Image {self.background} Not found please enter correct name of image")
        while True:
            self.scren.fill(self.bgcolor)
            self.scren.blit(bgimg, (0, 0))
            for eve in pygame.event.get():
                self.eve = eve
                if eve.type == pygame.QUIT:
                    exit()
            if self.target is not None:
                self.target()
            pygame.display.update()
            self.colock.tick(self.fps)


# ---------------------

if __name__ == "__main__":
    def test():
        print('gui')
    window = app(target=test)
    window.run()
