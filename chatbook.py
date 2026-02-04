class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""Welcome to ChatBook !!
                            How Would I help you
                         1.press 1 for signup
                         2.press 2 for signin
                         3.press 3 for write a post
                         4.press 4 for chat with friend
                         5.press anything for exit""")
        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.post_message()
        elif user_input=="4":
            self.sent_message()
        else:
            exit()
    
    def signup(self):
        self.username=input("enter email ->")
        self.password=input("enter Password->")
        print("signup successfully !!")
        self.menu()

    def signin(self):
        if self.username=="" and self.password=="":
            print("Signup First by selecting the 1st option")
        else:
         email=input("enter email ->")
         pwd=input("enter Password->") 
         if(email==self.username and pwd==self.password):
             print("login successful !!")
             self.loggedin=True
         else:
             print("invalid credentials !!")
        print('\n')
        self.menu()
    
    def post_message(self):
        if self.loggedin==True:
            txt=input("write a post")
            print(f"you post has been posted ->{txt}")
        else:
            print("Firstly signin the account")
        print('\n')
        self.menu()
    
    def sent_message(self):
        if self.loggedin==True:
            mes=input("type a message ->")
            frind=input("whom wants to send you a message")
            print(f"message sent succesfully to the {frind}")
        else:
             print("Firstly signin the account")
        print('\n')
        self.menu()
    
