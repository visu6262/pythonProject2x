class password:
    def __init__(self):
        self.phone=8877
        self._mail="admin1234"
        self.__bank="bank1234"
        self.__laptop=8888
        print("your phone password is:",self.phone)

    def mail(self):
        print("Y r mail pwd is:",self._mail)

    def bank(self):
        print("you are bank pwd is:",self.__bank)

    def laptop(self):
        print("Y r laptop pwd is:",self.__laptop)

you=password()
you.mail()
you.bank()
you.laptop()