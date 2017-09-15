from clcrypto import password_hash


class User:

    __id = None
    email = None
    username = None
    __hashed_password = None

    cnx = None

    def __init__(self):
        self.__id = -1
        self.username = ""
        self.email = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, raw_password, salt):
        self.__hashed_password = password_hash(raw_password, salt)

    def save(self):
        if self.__id == -1:
            cursor = self.cnx.cursor()
            sql = """insert into `User` (username, email, hashed_password)
                     values (%s, %s, %s)"""
            values = (self.username, self.email, self.__hashed_password)
            cursor.execute(sql, values)
            self.cnx.commit()
            self.__id = cursor.lastrowid
            return True
        return False
