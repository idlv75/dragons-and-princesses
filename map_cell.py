
class MapCell():
    def __init__(self, cell_type, amount):
        self.__cell_type = cell_type
        self.__amount = amount

    @property
    def cell_type(self):
        return self.__cell_type

    @property
    def amount(self):
        return self.__amount

    @cell_type.setter
    def cell_type(self, c_type):
        self.__cell_type = c_type

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

