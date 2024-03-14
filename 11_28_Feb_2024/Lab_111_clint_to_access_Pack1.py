import sys
sys.path.append("/11_28_Feb_2024/pack1")

import display
import show
a=display.show()
a=show.show()

print("-------------")

from display import show
a=show()

from show import show
a=show()