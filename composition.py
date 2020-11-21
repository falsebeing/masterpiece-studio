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
		self.file_name = name.replace(" ", "_")
		self.rhythm = durationsre.Rhythm(measures, timesig)

		self.extended_filepath = extended_filepath + "/" + self.file_name
		self.pdf = pdf
		self.midi = midi

		self.notation = pitchesre.Notation(key, key_scale, left_limits, right_limits, self.rhythm, None, 1, None)

		self.write_ly(lywrite_content())


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
		if self.pdf:
			subprocess.call(["lilypond", "long.ly"])

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

	def write_ly(content):
	    file = open(f'output/{self.extended_filepath}{self.file_name}.ly', 'w')
	    file.write(content)
	    file.close


# def compose():
# 	notation = pitchesre.Notation("d", "major",['g', "c'''''"], ['a,,,', "f'"], test_rhythm, None, 1, None)
# 	test_rhythm.display_hand_patterns()
# 	right_composition = ""
# 	left_composition = ""
# 	for n in notation.right_notation:
# 		if "|" in n:
# 			print(f"Adding {n}")
# 			right_composition = right_composition + f'{n} '
# 		else:
# 			print(f"Adding {n}")
# 			right_composition = right_composition + f'{n} '

# 	for n in notation.left_notation:
# 		if "|" in n:
# 			print(f"Adding {n}")
# 			left_composition = left_composition + f'{n} '
# 		else:
# 			print(f"Adding {n}")
# 			left_composition = left_composition + f'{n} '

# 	print(f"Right: {right_composition}") 
# 	print(f"Left: {left_composition}")
# 	return right_composition, left_composition


# right_hand, left_hand = compose()



if __name__ == "__main__":

	print(right_hand)
	create_ly(content, 'test11')
	#
	# file = open('testly.ly', 'w')
	#
	# file.write(content)
	# file.close
