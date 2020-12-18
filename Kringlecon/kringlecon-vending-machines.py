#This script was used to solve the cipher for the vending machine password
#for KringleCon 2020


#This was used to generate the string of all alphanumeric characters
#for the unencrypted password
#
#print(*filter(str.isalnum,map(chr,range(123))),sep='')


all_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#This string was obtained from vending-machine.json as the post-encryption
#version of the above unencrypted password

unencrypted_password = ""

#It turns out each letter of the unencrypted letter is assigned an encrypted letter based on both
#the original letter and the index of that letter in the password, rotating through a total of 8 variants
#For example, a password of 16 0's (0000000000000000) yields an encrypted version of 3ehm9ZFH3ehm9ZFH
#Therefore to generate a complete dictionary a string of all characters repeated 8 times (one for each index
#variant) was necessary and is generated below

for char in all_chars:
    unencrypted_password += char*8
    
#This was the decrypted password generated from the unencrypted password above
encrypted_password = "3ehm9ZFH2rDO5LkIpWFLz5zSWJ1YbNtlgophDlgKdTzAYdIdjOx0OoJ6JItvtUjtVXmFSQw4lCgPE6x7XiGRehmwDqTpKv7fLbn3UP9Wyv09iu8Qhxkr3zCnHYNNLCeOSFJGRBvYPBubpHYVzka18jGrEA24nILqF14D1GnMQKdxFbK363iZBrdjZE8IMJ3ZxlQsZ4Uisdwjup68mSyVX10sI2SHIMBo4gC7VyoGNp9Tg0akvHBEkVH5t4cXy3VpBslfGtSz0PHMxOl0rQKqjDq2KtqoNicv9VbtacpgGUVBfWhPe9ee6EERORLdlwWbwcZQAYue8wIUrf5xkyYSPafTnnUgokAhM0sw4eOCa8okTqy1o63i07r9fm6W7siFqMvusRQJbhE62XDBRjf2h24c1zM5H8XLYfX8vxPy5NAyqmsuA5PnWSbDcZRCdgTNCujcw9NmuGWzmnRAT7OlJK2X7D7acF1EiL5JQAMUUarKCTZa"

decryption_dict = {}

#Store the encrypted character and its index (modulo 8) as a key for the unencrypted character
for i in range(len(unencrypted_password)):
    decryption_dict[encrypted_password[i]+str(i%8)] = unencrypted_password[i]

password_to_decrypt = "LVEdQPpBwr"
decrypted_password = ""

for i in range(len(password_to_decrypt)):
    decrypted_password += decryption_dict[password_to_decrypt[i]+str(i%8)]

print(decrypted_password)
