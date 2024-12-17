#Braden Leach
#December 16 2024
#Password Validation

password = input('What is your password: ')

#----part one----#

 #Check length
def check_length(password):
    if len(password) < 8:
        return 'Password must be at least 8 characters long.' 
    return None 
    

 # Check First Five
def check_first_five(password):
  if len(password) >= 5 and not password[0:5].isalpha():
      return'The first five characters must be letters only!'
  return None
    

     #Check Last Three
def check_last_three(password):
    if len(password) >= 3 and not password[-3:].isdigit():
       return 'The last three characters must be numbers only!'
    return None
    



#----part two----# 

#Check special letter 
def check_no_special_letters(password):
   special_caracter = '~`!@#$%^&*()_+-={}[]:";\'<>?,./'
   
   for char in password: 
      if char in special_caracter:
         return 'Sorry password can not contain any special characters!'
   return None