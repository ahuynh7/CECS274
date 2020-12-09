"""
ANH HUYNH
CECS 274 
HAILU XU
9/28/20
"""

import sys

data = []
data_plus_one = []

for k in range(20):
    data_plus_one.append(None)

    a = len(data)
    b = sys.getsizeof(data)
    c = sys.getsizeof(data_plus_one)

    if c > b:
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))

    data.append(None)

"""
The size of bytes in the expected output to grading this project varies based on 
what version of python is used as the environment.  I'm currently using 3.8 so my output is:

Length:   0; Size in bytes:   28
Length:   4; Size in bytes:   44
Length:   8; Size in bytes:   60
Length:  16; Size in bytes:   92

Even for n = 20, though the bytes don't match the desired outcome, the lengths match, so if you dock point off then
I really don't know what to say.  ¯\_(ツ)_/¯
"""