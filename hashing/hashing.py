#so ,let's just imagine that intruder got access of our db and now he has like all user passwords
#to prevent this we have to hash passwords , it converts password into string-cipher and the feature is this cipher cannot be returned
#to the first string-password which was created by user

import bcrypt
#1)#first of all we translate password into bytes:
password = "user_password".encode("utf-8")
#but what if user have like the same passwords in the beginning? - as resolution we use gensalt() which makes even similar passwords
#2)#have different hash-cipher - and in outcome even similar passwords will have different and unique hash-ciphers
salt = bcrypt.gensalt() #UNIQUE HASH
#3)now we are hashing , here we get byte-hashing:
hashed_password = bcrypt.hashpw(password,salt)
#4)#afte that we have to convert this byte-hashing into string-hashing , that's it:
hashed_password_string = hashed_password.decode('utf-8')
print(hashed_password_string)

############
#when user log in , we simply compare two hashes(user's hash and db hash)
entered_password = "user_password".encode("utf-8")
db_hash = hashed_password_string.encode("utf-8")
#AND HERE WE COMPATE THEM BOTH :
is_correct = bcrypt.checkpw(entered_password,db_hash)
print(is_correct)
