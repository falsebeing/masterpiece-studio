upper = {
  \clef treble
  \key c \major
  \time 4/4
  
g,,8  d,,8~  d,,8  e,,8~  e,,2~  | e,,4~  e,,8  c,8~  c,8  g,,8  c,16  e,8  d,16~  | d,8  a,,8~  a,,16  c,8  e,16~  e,8.  d,32  b,,32  a,,4  | b,,2  d,4  c,4~  | c,2  b,,2  | d,,8  g,,64  f,,64  c,,16.~  c,,2~  c,,8~  c,,32  f,,16.~  | f,,32  a,,16.  c,8~  c,2~  c,8  d,8  | a,,8  g,,8~  g,,8  e,,8  b,,,8  d,,8  d,4  | a,,8  f,,8  g,,4  d,4  e,4~  | e,4  g,,8  f,,8~  f,,8  e,,8~  e,,4~  | e,,8  a,,8~  a,,2.~  | a,,8  e,,64  b,,64  d,16.~  d,8~  d,32  f,16.~  f,32  d,8..~  d,32  g,,8  e,,16.~  | e,,32  a,,8..~  a,,32  f,,8..~  f,,8~  f,,32  f,16.~  f,8~  f,32  c16.~  | c2~  c8~  c32  d16.~  d4~  | d2~  d8~  d32  b,16.~  b,4~  | b,32  g,8..~  g,8~  g,32  c,16.  c4  d32  g,8  b,16.  | 
}

lower = {
  \clef bass
  \key c \major
  \time 4/4

a4  e'4  d'2  | b4  c'4  g'2~  | g'4  f'4  e'4  c'4  | g8  c8~  c8  a16.  f32~  f4~  f16.  c8  b,32~  | b,4~  b,8..  f,32~  f,2~  | f,8..  d32~  d4~  d8..  a32~  a8..  d'32~  | d'16  c'8.  e'2  c'8  f8~  | f8  c8~  c8  f8~  f8  a,8  c4  | e4  c'4  b64  g64  d8..~  d4~  | d32  b,8..~  b,4~  b,32  c,8..~  c,32  g,8..~  | g,2~  g,32  d64  e,64  d,64  b,,64  e,16  b,,32  c,16~  c,32  d,8  g,,16.~  | g,,8~  g,,32  f,,16.~  f,,16.  e,,8~  e,,32~  e,,16.  c,8  f,,32~  f,,4~  | f,,16.  e,,8~  e,,32~  e,,16.  a,,,8~  a,,,32~  a,,,2~  | a,,,16.  c,,8~  c,,32~  c,,16.  f,,8~  f,,32~  f,,16.  e,8~  e,32~  e,4~  | e,2~  e,16.  b,,8  b,64  d64  g4  | a8  c'8~  c'8  a8~  a8  c'8~  c'4  | 
}

\score {
  \new PianoStaff <<
    \set PianoStaff.instrumentName = #"Piano  "
    \new Staff = "upper" \upper
    \new Staff = "lower" \lower
  >>

			\layout { }
			\midi { }
		}