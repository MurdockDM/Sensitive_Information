class Patient:

    def __init__(self, social_security, date_of_birth, account_number, first_name, last_name, address):
        self.__social_security = social_security
        self.__date_of_birth = date_of_birth
        self.__account_number= account_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address


    # First three properties of Patient need to be read only

    @property
    def social_security(self):
        try:  
            return self.__social_security
        except AttributeError:
            return 0 
    
    @property
    def date_of_birth(self):
        try:  
            return self.__date_of_birth
        except AttributeError:
            return 0 
    
    @property
    def account_number(self):
        try:  
            return self.__account_number
        except AttributeError:
            return 0 

    # First name and last name should not be exposed at all but instead
    # calculate and expose a  full_name property

    @property
    def full_name(self):
        try:
            return self.__first_name + " " + self.__last_name
        except AttributeError:
            return 0

    # Address needs to have a getter and a setter

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return 0

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError("Please provide a string value for the address")                        

                