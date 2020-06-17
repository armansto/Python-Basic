class User:
    Name = ""
    Email = ""
    Password = ""
    Login = False

    def Login(self):
        Email = input("Enter email ID: ")
        Password = input("Enter Password: ")

        if Email == self.Email and Password == self.Password:
            Login = True
            print("Login Successful.")
        else:
            print("Login Failed!")

    def Logout(self):
        Login =  False
        print("Logged Out!")

    def IsLoggedIn(self):
        if self.Login:
            return True
        else:
            return False

    def Profile(self):
        if self.IsLoggedIn():
            print(self.Name,"\n",self.Email)
        else:
            print("User is not logged in")

User1 = User()
User1.Name = "Sayed"
User1.Email = "Sayed@test.com"
User1.Password = "123456"

User1.Login()
User1.Profile()

Hello = input()