class Recover:
    def __init__(self, user, password, r_password):
        self.__user= user
        self.__password = password
        self.__r_password = r_password

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password= password

    @property
    def r_password(self):
        return self.__r_password
    @r_password.setter
    def r_password(self, r_password):
        self.__r_password = r_password