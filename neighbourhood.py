'''
    Kay (Mengxian) Cai
    CS5001, Fall 2022
    Data Dashboard Final Project - Milestone 1
    neighbourhood.py -- store the class of Neighbourhood
'''
HECTARRE_TO_SQUAREMETRE = 10000

class Neighbourhood:
    '''
    class: Neighbourhood
        A Neighbourhood has a name and population. It knows to count how many parks in
        this Neighbourhood and calculate the total area of all parks in it. It also knows
        how to sort its Parks in different order (alphabetically or based on size of park
        area ascendingly or descendingly).
    Attributes: name, population, parks, parks_area
    Methods: change_population, add_park, count_parks, calculate_parks_area_per_person_sqm,
        sort_parks_area_ascendingly, sort_parks_area_descendingly, sort_parks_name_alphabetically
    '''

    def __init__(self, name, population = 0):
        '''
        Constructor -- to create new instances of Neighbourhood.
        Parameters:
            self -- the current Neighbourhood instance
            name -- a string, which is the name of the Neighbourhood
            population -- an integer, which is the number of total population in this
            Neighbourhood, optional and default is 0
        Raise:
            TypeError if name is not string, or if population is not an integer  
            ValueError if population is a negative number.
        '''
        if not isinstance(name, str):
            raise TypeError("The name of a Neighbourhood must be a string.")
        if not isinstance(population, int):
            raise TypeError("The population of a Neighbourhood must be an integer.")
        if population < 0:
            raise ValueError("The population of a Neighbourhood cannot be a negative number.")
        self.name = name
        self.population = population
        self.parks = list()
        self.parks_area = 0
        self.parks_num = None
        self.area_person_sqm = None


    def change_population(self, new_population):
        '''
        Method -- to change the population of the current Neighbourhood instance.
        Parameters:
            self -- the current Neighbourhood instance
            new_population -- an integer, which is the new population of this Neighbourhood
        Return:
            None
        Raise:
            TypeError if the new population is not an integer
            ValueError if the new population is a negative number
        '''
        if not isinstance(new_population, int):
            raise TypeError("The population of a Neighbourhood must be an integer.")
        if new_population < 0:
            raise ValueError("The population of a Neighbourhood cannot be a negative number.")
        self.population = new_population


    def add_park(self, park):
        '''
        Method -- to add a Park into the current Neighbourhood instance.
        Parameters:
            self -- the current Neighbourhood instance
            park -- a Park object 
        Return:
            None
        Raise:
            TypeError if a non-Park object is given as parameter
        '''
        from park import Park
        if not isinstance(park, Park):
            raise TypeError("This method only takes a Park object.")
        for existing_park in self.parks:
            if existing_park.name == park.name:
                raise ValueError("This park already exists.")
            else:
                continue
        self.parks.append(park)
        self.parks_area += park.area


    def count_parks(self):
        '''
        Method -- to count the total number of Parks in the current Neighbourhood
        instance.
        Parameters:
            self -- the current Neighbourhood instance
        Return:
            an integer, which is the total number of Parks in the current
            Neighbourhood instance
        Raise:
            None
        '''
        park_num = len(self.parks)
        self.parks_num = park_num


    def calculate_parks_area_per_person_sqm(self):
        '''
        Method -- to calculate the area of parks per person of the current
        Neighbourhood instance by dividing the total park area with population
        of this Neighbourhood. The total park area is denominated in hectare, and
        will be converted to squaremetres for calculation. 
        Parameters:
            self -- the current Neighbourhood instance
        Return:
            a float, which represents the area of parks per person 
        Raise:
            ZeroDivisionError if the population is zero
        '''
        if self.population == 0:
            raise ZeroDivisionError("This Neighbourhood has zero population.")
        area_per_person = self.parks_area * HECTARRE_TO_SQUAREMETRE / self.population
        self.area_person_sqm = area_per_person


    def sort_parks_area_ascendingly(self):
        '''
        Method -- to sort all Parks in this Neighbourhood by the ascending order in terms of
        the area of each park. The Park with the largest area will be the last item in the
        sorted list.
        Parameters:
            self -- the current Neighbourhood instance
        Return:
            "No parks" reminder if no Parks in this Neighbourhood 
        Raise:
            None
        '''
        parks_len = len(self.parks)
        if parks_len == 0:
            return "No Parks in this Neighbourhood."
        else:
            for i in range(1, parks_len):
                current = self.parks[i]
                j = i - 1
                while j >= 0 and self.parks[j].area > current.area:
                    self.parks[j + 1] = self.parks[j]
                    self.parks[j] = current
                    j -= 1


    def sort_parks_area_descendingly(self):
        '''
        Method -- to sort all Parks in this Neighbourhood by the descending order in terms of
        the area of each park. The Park with the smallest area will be the last item in the
        sorted list.
        Parameters:
            self -- the current Neighbourhood instance
        Return:
            "No parks" reminder if no Parks in this Neighbourhood 
        Raise:
            None
        '''
        parks_len = len(self.parks)
        if parks_len == 0:
            return "No Parks in this Neighbourhood."
        else:
            for i in range(1, parks_len):
                current = self.parks[i]
                j = i - 1
                while j >= 0 and self.parks[j].area < current.area:
                    self.parks[j + 1] = self.parks[j]
                    self.parks[j] = current
                    j -= 1


    def sort_parks_alphabetically(self):
        '''
        Method -- to sort all Parks in this Neighbourhood by the alphabetical order in terms
        of the first letter of the name of each park. 
        Parameters:
            self -- the current Neighbourhood instance
        Return:
            "No parks" reminder if no Parks in this Neighbourhood 
        Raise:
            None
        '''
        parks_len = len(self.parks)
        if parks_len == 0:
            return "No Parks in this Neighbourhood."
        else:
            for i in range(parks_len):
                for j in range(i + 1, parks_len):
                    if ord(self.parks[i].name[0]) > ord(self.parks[j].name[0]):
                        temp = self.parks[i]
                        self.parks[i] = self.parks[j]
                        self.parks[j] = temp


    def __str__(self):
        '''
        Method -- to return a string that represents this Neighbourhood.
        Parameters:
            self -- the current Neighbourhood instance
        Return:
            a string that represents this Neighbourhood
        Raise:
            None
        '''
        printable = f"{self.name} Neighbourhood"
        return printable        


    def __eq__(self, other):
        '''
        Method -- to compares the current Neighbourhood instance to another one.
        Parameters:
            self -- the current Neighbourhood instance
            other -- the other Neighbourhood instance
        Return:
            Boolean True if the name of two Neighbourhoods are the same, otherwise,
            return Boolen False
        Raise:
            TypeError if the other is not a Neighbourhood instance
        '''
        if not isinstance(other, Neighbourhood):
            raise TypeError("You can only compare two Neighbourhoods.")
        else:
            return self.name == other.name            
        
