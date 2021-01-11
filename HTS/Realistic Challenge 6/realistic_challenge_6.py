file = open('encrypted.txt','r')
encrypted_text = file.read()

split_text = encrypted_text.split('.')
for i in range(len(split_text)):
    split_text[i] = split_text[i].strip()

# estimate initial chr_offset from the password by assuming first letter is 'a'
chr_offset = -97
for i in range(1,4):
    chr_offset += int(split_text[i])


def decode(chr_offset):
    output_str = ''
    chr_sum = 0
    for i in range(1,len(split_text)):
        if i%3 != 0:
            chr_sum += int(split_text[i])
        else:
            chr_sum += int(split_text[i])
            output_str += chr(chr_sum - chr_offset)
            chr_sum = 0
    return output_str

print(decode(chr_offset))
done = input('Is this right? Input yes if so, otherwise hit enter: ')
if done == 'yes':
    done = True
while done != True:
    chr_offset += 1
    print(decode(chr_offset))
    done = input('Is this right? Input yes if so, otherwise hit enter: ')
    if done == 'yes':
        done = True


print('Your offset was: ' + str(chr_offset))
password_guess = ''
guess_offset = 0
while True:
    if guess_offset + 97 < chr_offset:
        guess_offset += 97
        password_guess += 'a'
    else:
        password_guess += chr(chr_offset - guess_offset)
        break
    
print('This would work as the encryption password: '+password_guess)
