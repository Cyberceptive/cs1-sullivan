module Box

import bool

data Box = mkBox bool

unbox: Box -> bool
unbox (mkBox b) = b

