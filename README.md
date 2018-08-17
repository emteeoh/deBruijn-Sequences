A deBruijn sequence of span _n_ is a periodic sequence in which every possible
_n_-tuple over the alphabet occurs exactly once.

In this project, I created both a sequence generator and a decoder.

deBruijns can be in any base (that's why i used "alphabet" in the first sentence)
but I'm only interested in binary at the moment, so
most of this code assumes binary.

#### Papers
* Lempel 1992.pdf: Describes a method of construction of a deBruijn
 sequence with an _n+1_ span from an _n_-span sequence. Also allows
 such sequences to be efficiently decoded.
* Mitchell.pdf:  Describes a method of construction of deBruijn sequences
that can then be decoded. Mitchell's construction builds _2n_-span sequences
from _n_-span sequences, and allows for recursive application and decoding to work with large dataset sizes.
* Patterson 1995.pdf
* The_Art_of_Computer_Programming - Vol 1.pdf
* tuliani2001.pdf
##### Generators
* Mitchell.py generates a sequence of span _2n_ from a sequence
span of _n_ . It's structured as a python iterator.
* KnuthAlgorithmR.py generates a sequence of span _n+1_ from a sequence
of span _n_ . It's structured as a python iterator.
* generate.py is an iterator that uses the above 2 iterators to generate a sequence of
any desired length. Import this file and call "iterbruijn(n)" to get a sequence of span _n_
* deBruijn.py is just a constant definition.
##### Scratch
This folder is where I'm putting old code experiments I don't want to
actually delete for whatever reason. Some of them worked until I broke them,
some never worked, some work but I don't like how they work.
### The Maths
A deBruijn is an infinite recurring sequence, but we usually just write down one round of the recurrence. Eg:
...0011001100110011... is a span 2 deBruijn, but we can really just write 0011 and remember that its effectively
circular. That also means we could write 1001, or 1100, or 0110. They're all the same, effectively.<p>
I like to call a span-v deBruijn D<sub>v</sub>. Its much simpler than "Span-v deBruijn sequence". The length
of D<sub>v</sub> is always going to be 2<sup>v</sup><p>
We'll need to remember the location of the all-0-tuple and all-1-tuple for decoding purposes later.
These are called s and s<sup>'</sup> respectively.

[MitchellEtAl1996] talks about modifications to deBruijns:
###### Punctured deBruijn
If you take D<sub>v</sub>, find the v-tuple of all zeroes, and then remove one 0 from there, 
you're left with a sequence that has **almost** all possible v-tuples, called a punctured deBruijn. Let's call
this D<sup>'</sup><sub>v</sub>
###### Double-Punctured deBruijn
If you take a punctured deBruijn, find the v-tuple of all ones, and remove one 1 from there, you're left
with a double-punctured deBruijn sequence.  Let's call this D<sup>''</sup><sub>v</sub>
###### Enhanced deBruijn
[MitchellEtAl1996] never names but uses a sequence that rather than having a 0 and 1 removed as in 
a double-punctured deBruijn, **adds** a 0 and a 1. This yields a sequence that has all possible tuples,
but the all-zero and all-one tuples are in there twice. I call these "enhanced" deBruijns, but I write 
it as D<sup>+</sup><sub>v</sub>
###### [MitchellEtAl1996] Construction
Its actually pretty straight-forward. Start with a known D<sub>v</sub>. Create A=D<sup>''</sup><sub>v</sub>,
and B=D<sup>+</sup><sub>v</sub>. If the length of D<sub>v</sub> is n, then length of A is n-2, 
and the length of B is n+2. If you concatenate 1+n/2 copies of A, you'll get a sequence of the same 
length as n/2 -1 concatenated copies of B. <p> The construction method is:
 1. interleave these two sequences B and A, creating a sequence 2<sup>2n</sup>-4 long.
 2. find the v-2 tuple (1,0,1,0,...) and insert (1,0). The location of the (1,0,1,0...) v-tuple is another
 important value we need to remember. It's called T.
You're now left with D<sup>''</sup><sub>2v</sub>. From here, you can trivially generate D<sub>2v</sub> 
as well as D<sup>+</sup><sub>2v</sub>. With those, you can do another iteration and create D<sub>4v</sub>, etc.
###### [MitchellEtAl1996] Decoding
The algorithm as described by [MitchellEtAl1996] works only with double-punctured deBruijns constructed using
the above algorithm. Decoding looks convoluted, but is actually straight-forward. D<sup>''</sup><sub>2n</sub>
was built from 2 sequences A and B. If x is a 2n-tuple to be decoded, you decode by mapping even bits of x to one of
A or B, and the odd bits to the other. Since there are several copies each of A and B in
D<sup>''</sup><sub>2n</sub>, we end up with 2 simultaneous equations we need to solve. 2 equations, 1 unknown,
so it's not terribly hard to solve. There are several ways to map the even bits of x to A or B:
1. If the even bits are all 0 or all 1, then the even bits must map to B.
1. if the odd bits are all 0 or all 1, then the odd bits must map to B.
1. if both the even bits tuple and the odd bits tuple are at an even position within A, then the position
of x must be even, and the odd bits tuple maps to A.
1. if both the even bits tuple and the odd bits tuple are at an odd position within A, then the position
of x must be even, and the odd bits tuple maps to A. 
1. if the even bits tuple and odd bits tuple are of different parity, then the position of x must be odd,
and the odd bits tuple maps to B.

The above can be a little hard to follow. It certainly took me a few weeks to internalize. I found that
working through the construction and decoding methods on paper starting with D<sub>3</sub> helped a lot.
I'd welcome efforts to restate the above to make it easier to follow. 


##### Using the Code
At the moment, the code is asymmetric: it can generate deBruijns of any span greater than 2, but 
it cannot decode odd-sized deBruijns at all, and for even deBruijns, it actually works against 
double-punctured deBruijns with a span of 6 or larger, not a simple deBruijn... I consider these limits
bugs which I'm working around, for the moment.

###### To generate a deBruijn of any length:
```python
import generate
deBruijn_of_span_v = [y for y in generate.iterbruijn(v)]

```

###### To generate a double-punctured deBruijn suitable for decoding:
```python
import generate
double_punctured_deBruijn_of_span_v = [y for y in generate.iterdpdB(v)]

```


###### To decode:
```python
import MitchellDecode
position_of_x = MitchellDecode.MitchellDecode(x)

```

##### setup for using mouseImageFetch
you'll need to be able to connect to the mouse. you can either be root, or do the following:
<p>(from https://stackoverflow.com/a/31994168)
create a file in /etc/udev/rules.d, mine is named 50-RichardWazHeer.rules<p>
in it, put something like:<p>
ACTION=="add", SUBSYSTEMS=="usb", ATTRS{idVendor}=="04f3", ATTRS{idProduct}=="0235", MODE="666", GROUP="richard", PROGRAM="/bin/sh -c 'echo -n $id:1.0 >/sys/bus/usb/drivers/usbhid/unbind'"
 
sudo udevadm control --reload
sudo udevadm trigger

unplug and replug your mouse.