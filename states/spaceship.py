from states.Invaders_Game import *
from utils.font import *


"""
----------------------------------------------------------------------------------------------------
SpaceShip class which controls the ship that you want to choice in the game.
----------------------------------------------------------------------------------------------------
"""


class SpaceShipState(GameState):

    def __init__(self, game):
        super(SpaceShipState, self).__init__(game)
        SCREEN_W = 800
        SCREEN_H = 600
        self.optionState = None
        self.font = FontType("Ariel", 50, (255, 255, 255))
        self.font_text = FontType("Ariel", 25, (255, 255, 255))
        self.index = 0
        self.inputTick = 0
        self.OptionItems = ['Press Enter to select your spaceship']
        self.spaceships = ['../media/ship1.png', '../media/ship2.png', '../media/ship3.png', '../media/ship4.png',
                           '../media/ship5.png', '../media/ship6.png']
        self.mySpaceships = self.loadSpaceships(self.spaceships)
        self.surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))

    """
        Initialize the instance of state to move.
    """
    def setOptionState(self, state):
        self.optionState = state

    """
    Load array of ships and resized them for the game.
    """
    @staticmethod
    def loadSpaceships(spaceships):
        resized_backgrounds = []
        for spaceship in spaceships:
            pic = pygame.image.load(spaceship)
            pic = pygame.transform.scale(pic, (100, 100))
            resized_backgrounds.append(pic)
        return resized_backgrounds

    def update(self, gameTime):
        keys = pygame.key.get_pressed()
        if (keys[K_LEFT] or keys[K_RIGHT]) and self.inputTick == 0:
            self.inputTick = 250
            if keys[K_LEFT]:
                self.index -= 1
                self.draw(self.surface)
                if self.index < 0:
                    self.index = len(self.mySpaceships) - 1
            elif keys[K_RIGHT]:
                self.index += 1
                if self.index == len(self.mySpaceships):
                    self.index = 0
                self.draw(self.surface)
        elif self.inputTick > 0:
            self.inputTick -= gameTime

        if self.inputTick < 0:
            self.inputTick = 0

        if keys[K_RETURN]:
            self.game.changeState(self.optionState)  # go to option state
            self.game.spaceship = self.spaceships[self.index]

    def draw(self, surface):
        self.font.center(surface, "Spaceship", 48)
        surface.blit(self.mySpaceships[self.index], (350, 250))
        surface.blit(pygame.transform.scale(pygame.image.load('../media/right_arrow.png'), (70, 70)), (680, 250))
        surface.blit(pygame.transform.scale(pygame.image.load('../media/left_arrow.png'), (70, 70)), (60, 250))

        y = surface.get_rect().height - len(self.OptionItems) * 110
        self.font_text.draw(surface, self.OptionItems[0], 250, y)
