#Braden Leach
#December 16 2024
#Password Validation


password = input('What is your password: ')

#Today's Function
 #Check length
def check_length(password):
    if len(password) < 8:
        print('Password must be at least 8 characters long.')
    else: 
        return
    
 # Check First Five
def check_first_five(password):
  if len(password) > 5 and password.isalpha():
      print('The first five characters must be letters only!')
  else: 
   None
    







     #Check Last Three
def check_last_three(password):
    