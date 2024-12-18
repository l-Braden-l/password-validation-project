#Braden Leach
#December 16 2024
#Password Validation

#password = input('What is your password: ')




#----part one----#

#Check length
def check_length(password):
    if len(password) < 8:
        return 'Password must be at least 8 characters long.'
    return None 
    

#Check First Five
def check_first_five(password):
  if len(password) >= 5 and not password[0:5].isalpha():
      return 'The first five characters must be letters only!'
  return None
    

#Check Last Three
def check_last_three(password):
    if len(password) >= 3 and not password[-3:].isdigit():
       return 'The last three characters must be numbers only!'
    return None
    



# #----part two----# 

# #Check for letter 
def check_for_letter(password):
   for char in password:
      if char.isalpha():
         return None
   return 'Password must contain at least one letter!'
        

# #Check special letter 
def check_no_special_letters(password):
   special_caracter = '~`!@#$%^&*()_+-={}[]:";\'<>?,./'

   for char in password: 
      if char in special_caracter:
         return 'Sorry password can not contain any special characters!'
   return None


# #Check for numbers 
def check_for_number(password):
   for char in password:
      if char.isdigit():
         return None
   return 'Password must contain at least one number!'




#----part three----#

#run main part of code
def main():
   password = input('Please enter your password:\n')

   password_check = [check_length(password),
                     check_first_five(password),
                     check_last_three(password),
                     check_no_special_letters(password),
                     check_for_letter(password),
                     check_for_number(password)
                     ]
   

   # list of errors
   errors = []


   # loop through each result in password_check
   for result in password_check:
      if result is not None: #if there is a error
         errors.append(result) #add error to list of errors

   #print errors
   if errors:
      for error in errors:
         print(error)

         
   #print password if no errors
   else: 
      print(f'Your password is: {password}')


#checks if the scrips is not imported as a module
if __name__ == '__main__':
   main()