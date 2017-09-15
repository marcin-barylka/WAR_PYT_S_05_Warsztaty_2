from MySQLdb import connect

from clcrypto import generate_salt
from models import User

def conn():
    cnx = connect(host="localhost", user="root", password="coderslab",
                  database="warsztaty_2")
    return cnx

cnx = conn()

if __name__ == "__main__":
    u = User()
    u.cnx = cnx
    u.username = "Zdzisiek"
    u.email = "zdzisiek@monopolowy.pl"
    u.set_password("coderslab", generate_salt())
    print(u.id, u.email, u.username, u.hashed_password)
    # print(len(u.hashed_password))
    u.save()
    print(u.id, u.email, u.username, u.hashed_password)
    cnx.close()