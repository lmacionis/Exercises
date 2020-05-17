# If you’re intrigued by why floating point arithmetic is sometimes inaccurate, on a piece of paper,
# divide 10 by 3 and write down the decimal result. You’ll find it does not terminate, so you’ll need an
# infinitely long sheet of paper. The representation of numbers in computer memory or on your calculator has
# similar problems: memory is finite, and some digits may have to be discarded. So small inaccuracies creep in.
# Try this script:

import math

a = math.sqrt(2.0)
print(a, a*a)
print(a*a == 2.0)
