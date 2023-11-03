from MySQL03 import sqldir
import bcrypt
def passwordCheck(username, password):
    mySql = sqldir.SqlCommands()

    myresult = mySql.select("hsptlpassworddb", "userlogintbl", constraints=f"WHERE Username='{username}'")

    mylist = []
    for x in myresult:
        mylist.append(x)

    if not mylist:
        print("No Username Found")
        exit()
    else:
        # NEED TO HIDE THIS SOMEWHERE (THINKING OF STORING IT IN A TEXT FILE)
        salt = b'$2b$12$EaywnB2ci06Djd7eUEUCqe'

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
        else:
            print('Login: ', False)
