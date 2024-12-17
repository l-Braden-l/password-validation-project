#Braden Leach
#December 16 2024
#Password Validation

#password = input('What is your password: ')

#----part one----#

#Check length
def check_length(password):
    if len(password) < 8:
        print( 'Password must be at least 8 characters long.')
    return None 
    

#Check First Five
def check_first_five(password):
  if len(password) >= 5 and not password[0:5].isalpha():
      print('The first five characters must be letters only!')
  return None
    

#Check Last Three
def check_last_three(password):
    if len(password) >= 3 and not password[-3:].isdigit():
       print('The last three characters must be numbers only!') 
    return None
    



# #----part two----# 

# #Check for letter 
def check_for_letter(password):
   for char in password:
      if char.isalpha():
         return None
   print('Password must contain at least one letter!') 
        

# #Check special letter 
def check_no_special_letters(password):
   special_caracter = '~`!@#$%^&*()_+-={}[]:";\'<>?,./'

   for char in password: 
      if char in special_caracter:
         print('Sorry password can not contain any special characters!') 
   return None


# #Check for numbers 
def check_for_number(password):
   for char in password:
      if char.isdigit():
         return None
   print('Password must contain at least one number!') 

