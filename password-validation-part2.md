## Python: Password Validation Project (Part 2 of 3)

### Overview

You'll learn how to validate the user's password by using:

- a `while` loop
- a series of user-defined (custom) functions

Examples of checks the functions will run against the password include:

- Does the password contain at least one letter?
- Does the password contain at least one number?

### Today's Functions

Today you'll write three functions, all of which take one parameter, **password**

- the `check_no_special_characters( )` function
- the `check_for_letter( )` function
- the `check_for_number( )` function

### The `check_for_letter( )` Function

- Function checks if the password contains at least one letter  

- In the function body, use a `for` loop and the `in` operator to check each `char` in the `password`  

- Then do the following inside the `for` loop:

    - As part of an `if` statement, apply the `isalpha ( )` method to the `char` variable to check if the character is a letter  

    - Return `None` if a letter is found (meaning there was no error)

- Return "Password must contain at least one letter!" (error message if no letter is found)

### The `check_no_special_characters( )` Function

- Checks if the password contains only lowercase letters and digits (no symbols or special characters)  

- Just like the `check_for_letter( )` function, use a `for` loop and the `in` operator to check each character (`char`) in the `password`

- Then do the following inside the `for` loop:

    - As part of an `if` statement, use `not in` to check if the `char` is **not contained** in the string `abcdefghijklmnopqrstuvwxyz0123456789`; return the message "Password cannot contain special characters or symbols!" if a character other than those in the string is found

- **return** `None` to indicate that the password is valid


### The `check_for_number( )` Function

- Checks if the password contains at least one number

- Use a `for` loop and the `in` operator to check each character (`char`) in the `password`  

- Then do the following inside the `for` loop:  

    - As part of an `if` statement, apply the `isdigit ( )` method to the `char` variable to check if the character is a number  

    - Return `None` if a number is found (meaning there was no error)

- Return "Password must contain at least one number!" (error message if no number is found)
