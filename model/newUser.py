class NewUser:
    def __init__(self, name, registry, user, password, r_password):
        self.__name = name
        self.__registry = registry
        self.__user= user
        self.__password = password
        self.__r_password = r_password

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def registry(self):
        return self.__registry
    @registry.setter
    def registry(self, registry):
        self.__registry = registry
        
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