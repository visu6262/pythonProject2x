import sys
sys.path.append("C:/Users/91939/PycharmProjects/pythonProject2x/11_28Feb2024/pack1")

import display
import show
a=display.show()
a=show.show()

print("-------------")

from display import show
a=show()

from show import show
a=show()