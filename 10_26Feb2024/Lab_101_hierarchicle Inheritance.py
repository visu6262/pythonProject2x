class keyboad():
    def infomation(self):
        print("printin Keyboard information")

class numbers_info(keyboad):
    def numbers(self):
        print("1 2 3 4 5 6 7 8 9")

class alphonumaric_info(keyboad):
    def alphonumaric(self):
        print("a b c...z")


class spl_info():
    def spl_chr(self):
        print("!@#$%^&*()")
class spl_info2(spl_info):
    def spl_sim(self):
        print("{}[]<>,.?/_=")

class text_box_allows(keyboad,spl_info):
    def display(self):
        print("this info allows in this text box")

visu_txt_box=text_box_allows()
visu_txt_box.display()
visu_txt_box.infomation()
