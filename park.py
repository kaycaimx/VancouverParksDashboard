'''
    Kay (Mengxian) Cai
    CS5001, Fall 2022
    Data Dashboard Final Project - Milestone 1
    park.py -- store the class of Park
'''

class Park:
    '''
    class: Park
        A Park has a name. It knows which neighbourhood it is located and can be compared
        with other Parks (for area equality). 
    Attributes: name, location, area
    Methods: change_name, change_location, change_area
    '''

    def __init__(self, name, location = "", area = 0):
        '''
        Constructor -- to create new instances of Park.
        Parameters:
            self -- the current Park instance
            name -- a string, which is the name of the Park
            location -- a string, which is the name of neighbourhood where this Park locates,
            optional and default is "" 
            area -- an integer or a float, which is the area of this Park, optional and
            default is 0
        Raise:
            TypeError if either name or location is not string, or if area is not a number  
            ValueError if area is a negative number.
        '''
        if not isinstance(name, str):
            raise TypeError("The name of a Park must be a string.")
        if not isinstance(location, str):
            raise TypeError("The location of a Park must be a string of the neighbourhood name.")
        if not isinstance(area, int) and not isinstance(area, float):
            raise TypeError("The area of a Park must be an integer or a float.")
        if area < 0:
            raise ValueError("The area of a Park cannot be a negative number.")
        self.name = name
        self.location = location
        self.area = area


    def change_name(self, new_name):
        '''
        Method -- to change the name of the current Park instance.
        Parameters:
            self -- the current Park instance
            new_name -- a string, which is the new name of this Park
        Return:
            None
        Raise:
            TypeError if the new name is not a string
        '''
        if not isinstance(new_name, str):
            raise TypeError("The name of a Park must be a string.")
        self.name = new_name
        
    
    def change_location(self, new_location):
        '''
        Method -- to change the location of the current Park instance.
        Parameters:
            self -- the current Park instance
            new_name -- a string, which is the new location of this Park
        Return:
            None
        Raise:
            TypeError if the new location is not a string
        '''
        if not isinstance(new_location, str):
            raise TypeError("The location of a Park must be a string of the neighbourhood name.")
        self.location = new_location


    def change_area(self, new_area):
        '''
        Method -- to change the area of the current Park instance.
        Parameters:
            self -- the current Park instance
            new_area -- an integer or a float, which is the new area of this Park
        Return:
            None
        Raise:
            TypeError if the new area is not an integer or a float
            ValueError if the new area is a negative number
        '''
        if not isinstance(new_area, int) and not isinstance(new_area, float):
            raise TypeError("The area of a Park must be an integer or a float.")
        if new_area < 0:
            raise ValueError("The area of a Park cannot be a negative number.")
        self.area = new_area        


    def __str__(self):
        '''
        Method -- to return a string that represents this Park.
        Parameters:
            self -- the current Park instance
        Return:
            a string that represents this Park
        Raise:
            None
        '''
        printable = f"{self.name} in {self.location} with an area of {self.area} hectares"
        return printable


    def __eq__(self, other):
        '''
        Method -- to compares the current Park instance to another one.
        Parameters:
            self -- the current Park instance
            other -- the other Park instance
        Return:
            Boolean True if the areas of two Parks are equal, otherwise, return Boolen False if
            areas are inequal
        Raise:
            TypeError if the other is not a Park instance
        '''
        if not isinstance(other, Park):
            raise TypeError("You can only compare two Parks.")
        else:
            return self.area == other.area
