from states.Invaders_Game import *
from utils.font import *
"""
----------------------------------------------------------------------------------------------------
	InterstitialState
	
	Displays a message between screens. Can be used for ''Game over'' or ''Get ready'' style
	messages
----------------------------------------------------------------------------------------------------
"""


class InterstitialState(GameState):
	
	def __init__(self, game, msg, waitTimeMs, nextState):
		super(InterstitialState, self).__init__(game)
		self.nextState = nextState
		self.font = FontType("Ariel", 50, (255, 255, 255))
		self.message = msg
		self.previousTimer = waitTimeMs
		self.waitTimer = waitTimeMs
		
	def update(self, gameTime):
		self.waitTimer -= gameTime
		if self.waitTimer < 0:
			self.game.changeState(self.nextState)
			self.waitTimer = self.previousTimer
			
	def draw(self, surface):
		self.font.center(surface, self.message, surface.get_rect().height / 2)
