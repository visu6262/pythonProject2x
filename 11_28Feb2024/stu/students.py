class stu_details():
    def __init__(self,s_id,s_name,s_grade,s_class):
        self.s_id=s_id
        self.s_name=s_name
        self.s_grade=s_grade
        self.s_class=s_class
    def display(self):
        print(f"student id is:{self.s_id},Student Name is:{self.s_name},"
              f"as of now he/she get grade is:{self.s_grade},and class is:{self.s_class}")
