class emp_details():
    def __init__(self,empid,empname,empsal):
        self.emp_id=empid
        self.emp_name=empname
        self.emp_sal=empsal

    def display(self):
        print(f"emp id is: {self.emp_id},emp Name is: {self.emp_name},and emp sal is:{self.emp_sal}")

