import random
from custom_loggin import *

ALL_LY_NOTES = ['1.', '1', '2.', '2', '4.', '4', '8.', '8', '16.', '16', '32.', '32', '64']


# phasing - sections of the song with different parameters (eg speed up)

class Rhythm:
	def __init__(self, measures, timesig):


		self.measures = measures
		self.timesig = timesig

		



	def roll_phases(self):
		# based on measures, designates phased section of song
		# returns (start_measure, end_measure)
		pass