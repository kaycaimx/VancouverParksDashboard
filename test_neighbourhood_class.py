'''
    Kay (Mengxian) Cai
    CS5001, Fall 2022
    Data Dashboard Final Project - Milestone 1
    test_neighbourhood_class.py -- test suite for the class of Neighbourhood
'''
import unittest
from park import Park
from neighbourhood import Neighbourhood

class testNeighbourhood(unittest.TestCase):

    def test_init_basic_required_parameter_only(self):
        nbh1 = Neighbourhood("Downtown")
        self.assertEqual(nbh1.name, "Downtown")
        self.assertEqual(nbh1.population, 0)
        self.assertEqual(nbh1.parks, [])
        self.assertEqual(nbh1.parks_area, 0)
        self.assertEqual(nbh1.parks_num, None)
        self.assertEqual(nbh1.area_person_sqm, None)

    def test_init_basic_all_parameters(self):
        nbh1 = Neighbourhood("Mount Pleasant", 123*100)
        self.assertEqual(nbh1.name, "Mount Pleasant")
        self.assertEqual(nbh1.population, 12300)
        self.assertEqual(nbh1.parks, [])
        self.assertEqual(nbh1.parks_area, 0)

    def test_init_bad_name_not_string(self):
        with self.assertRaises(TypeError):
            nbh1 = Neighbourhood(3)
            nbh2 = Neighbourhood(["Downtown"])
            nbh3 = Neighbourhood({"Downtown"})

    def test_init_bad_population_not_integer(self):
        with self.assertRaises(TypeError):
            nbh1 = Neighbourhood("Downtown", 400.0)
            nbh2 = Neighbourhood("Downtown", "400")
            nbh3 = Neighbourhood("Downtown", "four hundred")
            nbh4 = Neighbourhood("Downtown", (400))
            nbh5 = Neighbourhood("Downtown", [400])

    def test_init_bad_population_negative_number(self):
        with self.assertRaises(ValueError):
            nbh1 = Neighbourhood("Downtown", -500)

    def test_change_population_method(self):
        nbh1 = Neighbourhood("Downtown", 12345)
        self.assertEqual(nbh1.population, 12345)
        nbh1.change_population(54321)
        self.assertEqual(nbh1.name, "Downtown")
        self.assertEqual(nbh1.population, 54321)

    def test_change_population_bad_not_integer(self):
        nbh1 = Neighbourhood("Downtown", 12345)
        with self.assertRaises(TypeError):
            nbh1.change_population(543.21)
            nbh1.change_population("500")
            nbh1.change_population("fifty")
            nbh1.change_population((500))
            nbh1.change_population([500])

    def test_change_population_bad_negative_number(self):
        nbh1 = Neighbourhood("Downtown", 12345)
        with self.assertRaises(ValueError):
            nbh1.change_population(-12345)

    def test_add_park_method(self):
        nbh1 = Neighbourhood("Downtown", 12345)
        park1 = Park("Stanley Park", "Downtown", 123.45)
        park2 = Park("Arbutus Village Park", "Arbutus-Ridge", 100)
        nbh1.add_park(park1)
        nbh1.add_park(park2)
        self.assertEqual(len(nbh1.parks), 2)
        self.assertEqual(nbh1.parks[0].name, "Stanley Park")
        self.assertEqual(nbh1.parks[0].location, nbh1.name)
        self.assertEqual(nbh1.parks[0].area, 123.45)
        self.assertEqual(nbh1.parks[1].name, "Arbutus Village Park")
        self.assertEqual(nbh1.parks[1].location, "Arbutus-Ridge")
        self.assertEqual(nbh1.parks[1].area, 100)
        self.assertEqual(nbh1.parks_area, 223.45)
        
    def test_add_park_bad_non_park(self):
        nbh1 = Neighbourhood("Downtown", 12345)
        nbh2 = Neighbourhood("Kitsilano", 6789)
        with self.assertRaises(TypeError):
            nbh1.add_park(nbh2)
            nbh1.add_park("Park")

    def test_add_park_bad_duplicated_parks(self):
        nbh1 = Neighbourhood("Downtown", 12345)
        park1 = Park("Stanley Park", "Downtown", 123.45)
        nbh1.add_park(park1)
        with self.assertRaises(ValueError):
            nbh1.add_park(park1)

    def test_count_parks_method(self):
        nbh1 = Neighbourhood("Downtown", 12345)
        park1 = Park("Stanley Park", "Downtown", 123.45)
        park2 = Park("Arbutus Village Park", "Arbutus-Ridge", 100)
        nbh1.add_park(park1)
        nbh1.add_park(park2)
        nbh1.count_parks()
        self.assertEqual(nbh1.parks_num, 2)

    def test_calculate_parks_area_per_person_sqm_method(self):
        nbh1 = Neighbourhood("Downtown", 12345)
        park1 = Park("Stanley Park", "Downtown", 123.45)
        park2 = Park("Arbutus Village Park", "Arbutus-Ridge", 100)
        nbh1.add_park(park1)
        nbh1.add_park(park2)
        nbh1.calculate_parks_area_per_person_sqm()
        self.assertAlmostEqual(nbh1.area_person_sqm, 2234500/12345)

    def test_calculate_parks_area_per_person_sqm_bad_zero_population(self):
        nbh1 = Neighbourhood("Downtown")
        park1 = Park("Stanley Park", "Downtown", 123.45)
        park2 = Park("Arbutus Village Park", "Arbutus-Ridge", 100)
        nbh1.add_park(park1)
        nbh1.add_park(park2)
        with self.assertRaises(ZeroDivisionError):
            nbh1.calculate_parks_area_per_person_sqm()

    def test_sort_parks_area_ascendingly_basic(self):
        nbh1 = Neighbourhood("Downtown")
        park1 = Park("Arbutus Village Park", "D", 10.1)
        park2 = Park("Coopers' Park", "D", 20.2)
        park3 = Park("Nelson Park", "D", 30.3)
        park4 = Park("Stanley Park", "D", 40.4)
        park5 = Park("Willow Park", "D", 50.5)
        nbh1.add_park(park5)
        nbh1.add_park(park4)
        nbh1.add_park(park1)
        nbh1.add_park(park3)
        nbh1.add_park(park2)
        self.assertEqual(nbh1.parks[0].area, 50.5)
        self.assertEqual(nbh1.parks[1].area, 40.4)
        self.assertEqual(nbh1.parks[2].area, 10.1)
        self.assertEqual(nbh1.parks[3].area, 30.3)
        self.assertEqual(nbh1.parks[4].area, 20.2)
        nbh1.sort_parks_area_ascendingly()
        self.assertEqual(nbh1.parks[0].area, 10.1)
        self.assertEqual(nbh1.parks[1].area, 20.2)
        self.assertEqual(nbh1.parks[2].area, 30.3)
        self.assertEqual(nbh1.parks[3].area, 40.4)
        self.assertEqual(nbh1.parks[4].area, 50.5)        

    def test_sort_parks_area_ascendingly_no_parks(self):
        nbh1 = Neighbourhood("Downtown")
        self.assertEqual(nbh1.sort_parks_area_ascendingly(), "No Parks in this Neighbourhood.")

    def test_sort_parks_area_descendingly_basic(self):
        nbh1 = Neighbourhood("Downtown")
        park1 = Park("Arbutus Village Park", "D", 10.1)
        park2 = Park("Coopers' Park", "D", 20.2)
        park3 = Park("Nelson Park", "D", 30.3)
        park4 = Park("Stanley Park", "D", 40.4)
        park5 = Park("Willow Park", "D", 50.5)
        nbh1.add_park(park1)
        nbh1.add_park(park2)
        nbh1.add_park(park5)
        nbh1.add_park(park3)
        nbh1.add_park(park4)
        self.assertEqual(nbh1.parks[0].area, 10.1)
        self.assertEqual(nbh1.parks[1].area, 20.2)
        self.assertEqual(nbh1.parks[2].area, 50.5)
        self.assertEqual(nbh1.parks[3].area, 30.3)
        self.assertEqual(nbh1.parks[4].area, 40.4)
        nbh1.sort_parks_area_descendingly()
        self.assertEqual(nbh1.parks[0].area, 50.5)
        self.assertEqual(nbh1.parks[1].area, 40.4)
        self.assertEqual(nbh1.parks[2].area, 30.3)
        self.assertEqual(nbh1.parks[3].area, 20.2)
        self.assertEqual(nbh1.parks[4].area, 10.1)

    def test_sort_parks_area_descendingly_no_parks(self):
        nbh1 = Neighbourhood("Downtown")
        self.assertEqual(nbh1.sort_parks_area_descendingly(), "No Parks in this Neighbourhood.")

    def test_sort_parks_alphabetically_basic(self):
        nbh1 = Neighbourhood("Downtown")
        park1 = Park("Arbutus Village Park")
        park2 = Park("Coopers' Park")
        park3 = Park("Nelson Park")
        park4 = Park("Stanley Park")
        park5 = Park("Willow Park")
        nbh1.add_park(park4)
        nbh1.add_park(park3)
        nbh1.add_park(park5)
        nbh1.add_park(park2)
        nbh1.add_park(park1)
        self.assertEqual(nbh1.parks[0].name, "Stanley Park")
        self.assertEqual(nbh1.parks[1].name, "Nelson Park")
        self.assertEqual(nbh1.parks[2].name, "Willow Park")
        self.assertEqual(nbh1.parks[3].name, "Coopers' Park")
        self.assertEqual(nbh1.parks[4].name, "Arbutus Village Park")
        nbh1.sort_parks_alphabetically()
        self.assertEqual(nbh1.parks[0].name, "Arbutus Village Park")
        self.assertEqual(nbh1.parks[1].name, "Coopers' Park")
        self.assertEqual(nbh1.parks[2].name, "Nelson Park")
        self.assertEqual(nbh1.parks[3].name, "Stanley Park")
        self.assertEqual(nbh1.parks[4].name, "Willow Park")

    def test_sort_parks_alphabetically_no_parks(self):
        nbh1 = Neighbourhood("Downtown")
        self.assertEqual(nbh1.sort_parks_alphabetically(), "No Parks in this Neighbourhood.")

    def test_str_basic(self):
        nbh1 = Neighbourhood("Downtown", 12345)
        self.assertEqual(str(nbh1), "Downtown Neighbourhood")

    def test_eq_basic_with_neighbourhood(self):
        nbh1 = Neighbourhood("Downtown", 12345)
        nbh2 = Neighbourhood("Downtown", 54321)
        nbh3 = Neighbourhood("Kitsilano", 12345)
        self.assertTrue(nbh1 == nbh2)
        self.assertFalse(nbh1 == nbh3)
    
    def test_eq_bad_with_non_neighbourhood(self):
        nbh1 = Neighbourhood("Downtown", 12345)
        park1 = Park("Stanley Park")
        with self.assertRaises(TypeError):
            nbh1 == park1
            nbh1 == "Downtown"   

    
def main():

    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
