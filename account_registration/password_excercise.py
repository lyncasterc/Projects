class User:
    def __init__(self,username,password='password'):
        self.username = username
        self.password = password
# user methods
    def login(self,username,password):
        with open('accounts.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                if username+'\n' == line:
                    
                    password_index = lines.index(line)+1
                    
                    if password+'\n' == lines[password_index]:
                        # print(f'Welcome back, {username}')
                        return True
                        
                    elif password+'/n'!= lines[password_index]:
            
                        return False
            
            return False

    def change_password(self):
        file_name = "accounts.txt"

        def replace_line(file,old_line,new_line):
            f = open(file,'r')
            data = f.read()
            f.close()

            new_data = data.replace(old_line,new_line)

            f = open(file,'w')
            f.write(new_data)
            f.close

        old_password = input('Enter current password: ')
        while old_password!=self.password:
            print('The password you entered is incorrect.\n')

            old_password = input('Please try again: ')
        
        else: 
            new_password = input('Enter new password: ')
            self.is_password_valid(new_password)

            replace_line(file_name,old_password,self.password)
            
            print('Password changed.')

       

# registration methods 
    def is_username_valid(self):
        with open('accounts.txt','r') as f:
            for line in f:
                while self.username+'\n' == line:
                    self.username = input('Username already exists. Enter different username: ')
    
    def is_password_valid(self,password):
        min_password_length = 6

        while len(password) < min_password_length:
            print(f'Password must be at least {min_password_length} characters long\n')
            password = input('Enter new password: ')
        
        while not any(char.isdigit() for char in password):
            print('Password must contain at least one numeric character\n')
            password = input('Enter new password: ')

        password_confirm = input('Re-enter password: ')

        while password_confirm != password:
            password_confirm = input('Passwords do not match. Try again: ')
        else:
            self.password = password

    def register_user(self):
        with open('accounts.txt','a') as f:
            f.write(f"{self.username}\n{self.password}\n")
        print(f"Account registered. Welcome {self.username}!")



print('1. Register new account\n')
print('2. Log into account \n')
choice = input('Enter choice: ')

while choice != '1' and choice!= '2':
    print('invalid input')
    choice = input('Enter 1 to register account or 2 to login: ')

if choice == '1':
    username = input('Enter desired username: ')
    new_user = User(username)
    new_user.is_username_valid()

    password = input('Enter desired password: ')
    new_user.is_password_valid(password)

    new_user.register_user()

if choice == '2':
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    unconf_user = User(username)
    while not unconf_user.login(username, password):
        print('Your username and/or password do not match our records. Please Try again.\n')
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        unconf_user = User(username)
        unconf_user.login(username,password)
    else:    
        user = User(username, password)

        print(f'Welcome back, {user.username}!')
        print('Enter 1 to change password\n')
        print('Enter q to logout and exit\n')
        choice = input('Enter choice: ')

        while choice!='1' and choice!= 'q' and choice!='Q':
            choice = ('Invalid input. Try again: ')
        
        if choice == '1':
            user.change_password()
        
        else:
            pass
        
        # if choice


    


