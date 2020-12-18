#This short script was written to solve Basic Challenge #6
#The encryption took each letter of the original unencrypted password
#and replaced it with the character whose Unicode code point was
#equal to the original character's Unicode code point + the index of
#the character in the password

password_to_decrypt = "56cd4:>?"
decrypted_password = ""

for i in range(len(password_to_decrypt)):
    decrypted_password += chr(ord(password_to_decrypt[i])-i)
    
print(decrypted_password)
    
