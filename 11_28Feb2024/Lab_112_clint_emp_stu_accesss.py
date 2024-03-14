import sys
sys.path.append("C:/Users/91939/PycharmProjects/pythonProject2x/11_28Feb2024/emp")
sys.path.append("C:/Users/91939/PycharmProjects/pythonProject2x/11_28Feb2024/stu")

import empless
import students
obj=empless.emp_details(123,"visu",400000)
obj.display()

outobj=students.stu_details(10,"visu",'A',"10 class")
outobj.display()

print("----------")
from empless import emp_details

obj=emp_details(122,"visuvisu",500000)
obj.display()

from students import stu_details
obj=stu_details(10,"visu visuuuu",'A',"10")
obj.display()