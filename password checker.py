
#MAIN
#User Input (username and password)
print("Creating a New password")
username=input("Username:")
print("-"*100)

#Placeholder
check_lenghtU = False,
check_digitU = False,
check_lowerU = False,
check_upperU = False

#length (minimum 4 Characters)
if len(username) >= 4:
 check_lenghtU = True

 #Contains at least one digit
for char in username:
 if char.isdigit():
  check_digitU = True

#Contains at least one uppercase letter
 elif char.isupper():
  check_upperU = True

  #Contains at least one lowercase letter
 elif char.islower():
  check_lowerU = True

checksU = [check_lenghtU,
check_digitU,
check_lowerU,
check_upperU]

if all (checksU):
 print("USERNAME CREATED SUCCESSFULLY")

else:
 print("USERNAME is Not strong enoght")

if not check_upperU:
 print("At least one uppercase Character")

if not check_lenghtU:
 print("At least 4 Character")

if not check_digitU:
 print("At least one digit")

if not check_lowerU:
 print("At least one lowercase Character")


else:
 password=input("Password:")
print("-"*100)

    #Placeholder
symbols = "!@#$%^&*()_-+{}<>?/=|"
check_lenght = False
check_digit = False
check_lower = False
check_upper = False
check_symbol = False
check_no_spaces = False

#Security checks
#length (minimum 8 Characters)
if len(password) >= 8:
 check_lenght = True

#Contains no spaces
if ' ' not in password:
 check_no_spaces = True

#Contains at least one digit
for char in password:
 if char.isdigit():
  check_digit = True
  
#Contains at least one uppercase letter
 elif char.isupper():
  check_upper = True

#Contains at least one lowercase letter
 elif char.islower():
  check_lower = True

#Contains at least one special Character
 elif char in symbols:
  check_symbol = True

#Display Results
checks = [check_lenght,
check_digit,
check_lower,
check_upper,
check_symbol,
check_no_spaces
]

if all (checks):
 print("ACCOUNT CREATED SUCCESSFULLY")
       

else:
 print("PASSWORD is Not strong enoght")
if not check_lenght:
 print("At least 8 Character")

if not check_digit:
 print("At least one digit")

if not check_lower:
 print("At least one lowercase Character")

if not check_upper:
 print("At least one uppercase Character")

if not check_no_spaces:
 print("Not Space")











