'''
    Kay (Mengxian) Cai
    CS5001, Fall 2022
    Data Dashboard Final Project - Milestone 1
    test_park_class.py -- test suite for the class of Park
'''

import unittest
from park import Park

class testPark(unittest.TestCase):
    
    def test_init_basic_required_parameter_only(self):
        park1 = Park("Stanley Park")
        self.assertEqual(park1.name, "Stanley Park")
        self.assertEqual(park1.location, "")
        self.assertEqual(park1.area, 0)

    def test_init_basic_all_parameters(self):
        park1 = Park("Stanley Park", "Downtown", 400.5)
        self.assertEqual(park1.name, "Stanley Park")
        self.assertEqual(park1.location, "Downtown")
        self.assertAlmostEqual(park1.area, 400.5)

    def test_init_bad_name_not_string(self):
        with self.assertRaises(TypeError):
            park1 = Park(3)
            park2 = Park(["Stanley Park"])
            park3 = Park({"Stanley Park"})

    def test_init_bad_location_not_string(self):
        with self.assertRaises(TypeError):
            park1 = Park("Stanley Park", 3)
            park2 = Park("Stanley Park",["Downtown"])
            park3 = Park("Stanley Park", {"Downtown"})

    def test_init_bad_area_not_number(self):
        with self.assertRaises(TypeError):
            park1 = Park("Stanley Park", "Downtown", "400")
            park2 = Park("Stanley Park", "Downtown", "four hundred")
            park3 = Park("Stanley Park", "Downtown", (400))
            park4 = Park("Stanley Park", "Downtown", [400])

    def test_init_bad_area_negative_number(self):
        with self.assertRaises(ValueError):
            park1 = Park("Stanley Park", "Downtown", -5)

    def test_change_name_method(self):
        park2 = Park("Stanley Park", "Downtown", 100/3 + 200/3)
        self.assertEqual(park2.name, "Stanley Park")
        park2.change_name("Stacy Park")
        self.assertEqual(park2.name, "Stacy Park")
        self.assertEqual(park2.location, "Downtown")
        self.assertAlmostEqual(park2.area, 300/3)

    def test_change_name_method_bad_non_string(self):
        park2 = Park("Stanley Park", "Downtown", 100)
        with self.assertRaises(TypeError):
            park2.change_name(3)
            park2.change_name(["Stacy Park"])
            park2.change_name({"Stacy Park"})

    def test_change_location_method(self):
        park2 = Park("Stanley Park", "Downtown", 77 * 4)
        self.assertEqual(park2.location, "Downtown")
        park2.change_location("Kitsilano")
        self.assertEqual(park2.name, "Stanley Park")
        self.assertEqual(park2.location, "Kitsilano")
        self.assertEqual(park2.area, 308)

    def test_change_location_bad_non_string(self):
        park2 = Park("Stanley Park", "Downtown", 100)
        with self.assertRaises(TypeError):
            park2.change_location(3)
            park2.change_location(["Kitsilano"])
            park2.change_location({"Kitsilano"})

    def test_change_area_method(self):
        park2 = Park("Stanley Park", "Downtown", 123.45)
        self.assertEqual(park2.area, 123.45)
        park2.change_area(543.21)
        self.assertEqual(park2.name, "Stanley Park")
        self.assertEqual(park2.location, "Downtown")
        self.assertEqual(park2.area, 543.21)

    def test_change_area_bad_not_number(self):
        park2 = Park("Stanley Park", "Downtown", 100)
        with self.assertRaises(TypeError):
            park2.change_area("50")
            park2.change_area("fifty")
            park2.change_area((50))
            park2.change_area([50])

    def test_change_area_bad_negative_number(self):
        park2 = Park("Stanley Park", "Downtown", 100)
        with self.assertRaises(ValueError):
            park2.change_area(-5)

    def test_str_basic(self):
        park3 = Park("Stanley Park", "Downtown", 100.0)
        self.assertEqual(str(park3), "Stanley Park in Downtown with an area of \
100.0 hectares")

    def test_eq_basic_with_park(self):
        park4 = Park("Stanley Park", "Downtown", 100.0)
        park5 = Park("Arbutus Village Park", "Arbutus-Ridge", 100)
        park6 = Park("Stanley Park", "Downtown", 99)
        self.assertTrue(park4 == park5)
        self.assertFalse(park4 == park6)

    def test_eq_bad_with_non_park_object(self):
        park4 = Park("Stanley Park", "Downtown", 100.0)
        with self.assertRaises(TypeError):
            self.assertFalse(park4 == 100.0)


def main():

    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
