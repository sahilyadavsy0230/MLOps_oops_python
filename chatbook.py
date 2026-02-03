class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False

    def menu(self):
        user_input=input("""Welcome to ChatBook !!
                            How Would I help you
                         1.press 1 for signup
                         2.press 2 for signup
                         3.press 3 for write a post
                         4.press 4 for chat with friend
                         5.press anything for exit""")
        
        if user_input=="1":
            pass
        elif user_input=="2":
            pass
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()