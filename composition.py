import subprocess
import os

from custom_logging import *
import durationsre
import pitchesre


"""
LY_BLOCKs form a skeleton frame for lywriter notation
"""

LY_BLOCK_1 = """upper = {
  \\clef treble
  \\key c \\major
  \\time 4/4
  
"""

LY_BLOCK_2 = """
}

lower = {
  \\clef bass
  \\key c \\major
  \\time 4/4

"""

LY_BLOCK_3 = """
}

\\score {
  \\new PianoStaff <<
    \\set PianoStaff.instrumentName = #"Piano  "
    \\new Staff = "upper" \\upper
    \\new Staff = "lower" \\lower
  >>
"""




# ALL USER INPUT comes into this constructor
# constructor calls Rhythm and Notation constructors with user input
# holds methods for converting Notation object to content string for the Studio class to write to file
class Composition:
	def __init__(self, name, measures, timesig, key, key_scale, left_limits, right_limits, extended_filepath, pdf, midi):

		self.name = name
		self.filename = name.replace(" ", "_") + ".ly"
		self.rhythm = durationsre.Rhythm(measures, timesig)

		self.filepath = "output/" + extended_filepath
		self.pdf = pdf
		self.midi = midi

		self.notation = pitchesre.Notation(key, key_scale, left_limits, right_limits, self.rhythm, None, 1, None)



#	def __init__(self, key, key_scale, left_limits, right_limits, rhythm, accidental_freq, rest_freq, anchor_strength):
		self.write_ly(self.lywrite_content())


	def lywrite_content(self):
		rh_ly = self._lywrite_hand(self.notation.left_notation)
		lh_ly = self._lywrite_hand(self.notation.right_notation)
		content = LY_BLOCK_1 + rh_ly + LY_BLOCK_2 + lh_ly + LY_BLOCK_3
		# sort of assuming layout { } means build a pdf to lywriter
		if self.pdf:
			content += """
			\\layout { }"""
		if self.midi:
			content += """
			\\midi { }"""
		content += """
		}"""

		return content

	def _lywrite_hand(self, hand_notation):
		lywritten = ""
		for n in hand_notation:
			if "|" in n:
				print(f"Adding {n}")
				lywritten = lywritten + f'{n} '
			else:
				print(f"Adding {n}")
				lywritten = lywritten + f'{n} '
		return lywritten

	def write_ly(self, content):
		try:
			os.mkdir(self.filepath)
		except FileExistsError:
			pass
		file = open(self.filepath+self.filename, 'w')
		file.write(content)
		file.close()
		if self.pdf:
			os.chdir(self.filepath)
			subprocess.call(["lilypond", self.filename])
			os.chdir("../")
