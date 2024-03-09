class password:
    def __init__(self):
        self.phone=8877
        self._mail="admin1234"
        self.__bank="bank1234"
        self.__laptop=8888
        print("your phone password is:",self.phone)

    def mail(self,is_auth):
                print("Y r mail pwd is:",self._mail)

    def bank(self,bank_pwd,is_auth):
        if bank_pwd==1234 and is_auth==True:
            print("you are bank pwd is:",self.__bank)
        else:
            print("in valied pin enter u r not show bank pwd")

    def laptop(self,pin):
        if pin==1234 or pin==True:
            print("Y r laptop pwd is:",self.__laptop)
        else:
            print("y r not access to laptop pwd try again!")

you=password()
you.mail(True)
print("------------")

you.bank(12,True)
you.bank(1234,True)
print("------------")

you.laptop(123)
you.laptop(1234)
you.laptop(True)
you.laptop(False)