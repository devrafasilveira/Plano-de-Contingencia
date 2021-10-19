class Contingency:
    def __init__(self, pharmacy, room, professional, registry, datetime, bc1, bc2, bc3, bc4, qtr1, qtr2, qtr3, qtr4):
        self.__pharmacy = pharmacy
        self.__room = room
        self.__professional = professional
        self.__registry = registry
        self.__datetime = datetime
        self.__bc1 = bc1
        self.__bc2 = bc2
        self.__bc3 = bc3
        self.__bc4 = bc4
        self.__qtr1 = qtr1
        self.__qtr2 = qtr2
        self.__qtr3 = qtr3
        self.__qtr4 = qtr4
        
    @property
    def pharmacy(self):
        return self.__pharmacy
    @pharmacy.setter
    def pharmacy(self, pharmacy):
        self.__pharmacy = pharmacy
    
    @property
    def room(self):
        return self.__room
    @room.setter
    def room(self, room):
        self.__room = room
        
    @property
    def professional(self):
        return self.__professional
    @professional.setter
    def professional(self, professional):
        self.__professional = professional
        
    @property
    def registry(self):
        return self.__registry
    @registry.setter
    def registry(self, registry):
        self.__registry = registry
        
    @property
    def datetime(self):
        return self.__datetime
    @datetime.setter
    def datetime(self, datetime):
        self.__datetime = datetime

    @property
    def bc1(self):
        return self.__bc1
    @bc1.setter
    def bc1(self, bc1):
        self.__bc1= bc1

    @property
    def bc2(self):
        return self.__bc2
    @bc2.setter
    def bc2(self, bc2):
        self.__bc2 = bc2

    @property
    def bc3(self):
        return self.__bc3
    @bc3.setter
    def bc3(self, bc3):
        self.__bc3 = bc3

    @property
    def bc4(self):
        return self.__bc4
    @bc4.setter
    def bc4(self, bc4):
        self.__bc4 = bc4

    @property
    def qtr1(self):
        return self.__qtr1
    @qtr1.setter
    def qtr1(self, qtr1):
        self.__qtr1 = qtr1

    @property
    def qtr2(self):
        return self.__qtr2
    @qtr2.setter
    def qtr2(self, qtr2):
        self.__qtr2 = qtr2

    @property
    def qtr3(self):
        return self.__qtr3
    @qtr3.setter
    def qtr3(self, qtr3):
        self.__qtr3 = qtr3

    @property
    def qtr4(self):
        return self.__qtr4
    @qtr4.setter
    def qtr4(self, qtr4):
        self.__qtr4 = qtr4