A deBruijn sequence is a sequence of symbols wherein all subsets of a certain size occur exactly once in the sequence.

Eg: a binary 2-bit deBruijn is 0011. Its subsets are 00, 01, 11, and 10.
Eg: a binary 3-bit deBruijn is 00011101. Its subsets are 000, 001, 011, 111, 110, 101, 010, 100.

[Mitchel et Al, 1996], the Mitchell.pdf, explains algorithms to generate and decode deBruijn sequences. By decoding,
they mean "find the position in the sequence where a subset is". So for 00011101, 110 decodes to 4.

It's an interesting read, but I found I just couldn't manage to make the decoders work! So I sent an email to
Dr. Mitchell, and he suggested I look into Section 7.2.1.1 of Knuth's The Art Of Computer Programing, Vol 4A.

You can find a pre-print of the section in the pdf named "Knuth TAOCP 4A section 7.2.1.1 pre-Fascicle.pdf".
Algorithm R and D are generators. R takes an n-bit deBruijn, and builds an n+1-bit deBruijn. D takes an n-bit deBruijn
and builds a 2n-bit deBruijn.

ex99 is a decoder from Knuth, in the exercises.
