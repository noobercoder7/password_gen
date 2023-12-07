import random
import string

# Initialize an empty list to store individual characters of the password
password_list = []

# Get user input for the length and complexity of the password
pass_length = int(input("Enter the length of the password!!\n"))
pass_complexity = int(
    input("Select Complexity! \n1 for Low, \n2 for Medium, \n3 for High\n"))

# Check the complexity level chosen by the user and define the character set accordingly
if pass_complexity == 1:
    letters = string.ascii_letters

elif pass_complexity == 2:
    letters = string.ascii_letters + string.digits

elif pass_complexity == 3:
    letters = string.ascii_letters + string.digits + string.punctuation

else:
    print("Invalid Input!!! Try again.")
    exit()

# Generate the password by randomly selecting characters and appending them to the list
for n in range(pass_length):
    password_list.append(random.choice(letters))

# Join the list of characters to form the final password string
password = ''.join(password_list)

# Display the generated password
print(f"Your generated password is: {password}")
