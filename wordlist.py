import itertools
import string
import time

def password_wordlist(start_range = 8, end_range = 10, file_name = "brut.txt"):
    #chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '@' + '#' + '$' + '.'
    chars = string.digits
    attempts = 0
    file = open(file_name, 'a')

    for password_length in range(start_range, end_range):
        for guess in itertools.product(chars, repeat=password_length):
            attempts+=1
            guess = ''.join(guess)
            file.write(guess)
            file.write("\n")
            print(guess, attempts)
    file.close()


start_range = 8
end_range = 9
file_name = "wifi_passwd_8_num.txt"  #Type "wifi_passwd_numberofthepawwsd_numorchar"

start_time = time.time()
password_wordlist(start_range, end_range, file_name)
end_time = time.time()
print(end_time-start_time)

##### Code by Sajal Rastogi