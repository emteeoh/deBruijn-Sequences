A deBruijn sequence of span _n_ is a periodic
sequence in which every possible
_n_-tuple over the alphabet occurs exactly
once as a window starting within the minimal  generating cycle of the sequence.

In this project, I aim to create both a sequence generator and a decoder.
In fact, the generators already work. The decoder is a tougher nut to crack.

####Papers
* Lempel 1992.pdf: Describes a method of construction of deBruijn sequences.
I haven't read this one yet, but I expect it to show how to generate an _n+1_ span
sequence from an _n_-span sequence.
* Mitchell.pdf:  Describes a method of construction of deBruijn sequences
that can then be decoded. Mitchell's construction builds _2n_-span sequences
from _n_-span sequences.
* Patterson 1995.pdf
* The_Art_of_Computer_Programming - Vol 1.pdf
* tuliani2001.pdf
####Generators
* KnuthAlgorithmD.py generates a sequence of span _2n_ from a sequence
span of _n_ . It's structured as a python iterator.
* KnuthAlgorithmR.py generates a sequence of span _n+1_ from a sequence
of span _n_ . It's structured as a python iterator.
* generate.py is an iterator that uses the previous 2 to generate a sequence of
any desired length.
* deBruijn.py is just a constant definition.
####Scratch
This folder is where I'm putting old code experiments I don't want to
actually delete.
