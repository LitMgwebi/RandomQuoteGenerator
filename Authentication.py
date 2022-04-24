import calculator
class Authentication:
     
     def signup(username, password):
          fileUser = open("profiles.txt", "a")
          fileUser.write(username + "#" + password)
          
          print("")
          calculator.operation()
          fileUser.close()
          
     def login(username, password):
          fileUser = open("profiles.txt", "r")
     
          for lines in fileUser.readlines():
               line = lines.split('#')
               
               file_username = line[0]
               file_password = line[1]
               
               if username == file_username:
                    if password == file_password:
                         print("Welcome back, " + file_username)
                         print("")
                         calculator.operation();
                    else:
                         print("Your username or password is invalid.")                         
               else:
                    print("Your username or password is invalid.")
               
               
          fileUser.close()
     

auth_option = input(''' Welcome to the caluclator Login terminal.
                    
If you have a profile with us please Login.
If you do not have a profile with us, kindly Sign up.

What will you do?: ''')

print("")
username = input("Please enter your username: ")
password = input("Please enter your password: ")

if auth_option == "login" or auth_option == "Login" or auth_option == "log in":
     Authentication.login(username, password)
elif auth_option == "signup" or auth_option == "Signup" or auth_option == "sign up":
     Authentication.signup(username, password)