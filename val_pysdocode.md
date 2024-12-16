Python: Password Validation Project (Part 1 of 3)
Overview
You'll learn how to validate the user's password by using:

a while loop
a series of user-defined (custom) functions
Examples of checks the functions will run against the password include:

Does the password meet the minimum length requirement?
Does the password contain at least one special character (such as &, ^, etc.)?
Today's Functions
Today you'll write three functions, all of which take one parameter, password

the check_length( ) function
the check_last_three( ) function
the check_first_five( ) function
The check_length( ) Function
In the function body, use an if statement to check if the length of the password is less than 8 characters

If the password is too short, return a message that says: "Password must be at least 8 characters long."

If the password meets the length requirement, return None to indicate that the password is valid

The check_first_five( ) Function
Checks if the first five characters in the password are letters only

Write a compound condition that uses the logical operator AND to connect the two conditions that make up the compound condition

The pseudocode for the compound condition is as follows:

If the password length is greater than or equal to 5 AND the first five characters of the password are NOT letters, return "The first five characters must be letters only!" (HINT: The Python isalpha ( ) string method would be useful here!)

return None to indicate that the password is valid

The check_last_three( ) Function
Checks if the last three characters in the password are numbers only

Write a compound condition that uses the logical operator AND to connect the two conditions that make up the compound condition

The pseudocode for the compound condition is as follows:

If the password length is greater than or equal to 3 AND the last three characters of the password are NOT numbers, return "The last three characters must be numbers only!" (HINT: The Python isdigit ( ) string method would be useful here!)

return None to indicate that the password is valid