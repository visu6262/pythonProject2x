class Gmail_login():
    mailid=None
    password=None

    def submit(self,userid,password):
        self.mailid=userid
        self.password=password

    def submit_conformation(self):
        if self.password=="admin@123":
            print("login successfully")
        else:
            print("u r not auth person")

raju=Gmail_login()
raju.submit("aaa@gmail.com","admin@123")
raju.submit_conformation()

print("--------------")

hema=Gmail_login()
hema.submit("aaa@gmail.com","abc123")
hema.submit_conformation()