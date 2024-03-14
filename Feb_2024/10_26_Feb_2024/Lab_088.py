class Gmail_login():
    mailid=None
    password=None

    def __init__(self,userid,password):
        self.mailid=userid
        self.password=password

    def submit_conformation(self):
        if self.password=="admin@123":
            print("login successfully")
        else:
            print("u r not auth person")

raju=Gmail_login("aaa@gmail.com","admin@123")
raju.submit_conformation()