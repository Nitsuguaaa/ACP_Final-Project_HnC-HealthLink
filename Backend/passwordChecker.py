from MySQL03 import sqldir
import bcrypt

sql = sqldir.SqlCommands()
file = open(r"rsc\Lists\UserList\salt.txt", "rt")
salt = bytes(file.read(), encoding="utf=8")
def passwordCheck(username, password):

    mylist = sql.select("userlogintbl", constraints=f"WHERE username='{username}'")
    if not mylist:
        print("No Username Found")
        exit()
    else:
        # ENCRYPTING USER'S PASSWORD INPUT
        passing = password.encode('utf-8')
        userpass = bcrypt.hashpw(passing, salt)

        # ENCODING ENCRYPTED PASSWORD IN DB USERNAME MATCH
        dbinput = str(mylist[0][1])

        dbpass = dbinput.encode('utf=8')

        # BUILT IN CHECKER (NOT WORKING????)
        # result = bcrypt.checkpw(userpass, dbpass)

        # IF STATEMENT
        if userpass == dbpass:
            print('Login: ', True)
            return True
        else:
            print('Login: ', False)
            return False

def generateUser(username, password):
    encodedpw = password.encode('utf-8')
    hashed = bcrypt.hashpw(encodedpw, salt)
    sql.insert("userlogintbl", ("username", "password"), (username, hashed))
    print("Username Generated")
