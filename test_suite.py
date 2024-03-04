'''
    Kay (Mengxian) Cai
    CS5001, Fall 2022
    Data Dashboard Final Project - Milestone 2
    test_suite.py -- test suite
'''
import requests
from park import Park
from neighbourhood import Neighbourhood
from functions_file import *

PARKS_URL = "https://opendata.vancouver.ca/explore/dataset/parks/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
CENSUS_URL = "https://webtransfer.vancouver.ca/opendata/csv/CensusLocalAreaProfiles2016.csv"
TEST_PARK_DATA = [['ParkID', 'Name', 'Official', 'Advisories', 'SpecialFeatures', 'Facilities', 'Washrooms', 'StreetNumber', 'StreetName', 'EWStreet', 'NSStreet', 'NeighbourhoodName', 'NeighbourhoodURL', 'Hectare', 'GoogleMapDest\r'], ['1', 'Arbutus Village Park', '1', 'N', 'N', 'Y', 'N', '4202', 'Valley Drive', 'King Edward Avenue', 'Valley Drive', 'Arbutus-Ridge', 'https://vancouver.ca/news-calendar/arbutus-ridge.aspx', '1.41', '49.249783,-123.15525\r'], ['4', 'Park Site on Puget Drive', '0', 'N', 'N', 'N', 'N', '4309', 'Puget Drive', 'Puget Drive', 'MacDonald Street', 'Arbutus-Ridge', 'https://vancouver.ca/news-calendar/arbutus-ridge.aspx', '0.09', '49.247723,-123.168194\r'], ['10', 'Andy Livingstone Park', '1', 'N', 'N', 'Y', 'Y', '89', 'Expo Boulevard', 'Expo Boulevard', 'Carrall Street', 'Downtown', 'https://vancouver.ca/news-calendar/downtown.aspx', '4.21', '49.278923,-123.1055\r'], ['14', "Coopers' Park", '1', 'N', 'Y', 'Y', 'N', '1020', 'Marinaside Crescent', 'Nelson Street', 'Marinaside Crescent', 'Downtown', 'https://vancouver.ca/news-calendar/downtown.aspx', '1.71', '49.273253,-123.1139\r']]
TEST_NEIGHBOURHOOD_NAME = ["Arbutus-Ridge", "Downtown", "West End"]
TEST_POPULATION_LIST = [25000, 60000, 10000]

def main():

    #test split_string -- basic
##    print(split_string("this is a new line \n this is a new line \n test"))
    #test split_string - TypeError
##    print(split_string(["this is a new line \n this is a new line \n test"]))

    #test create_parks_list_of_lists -- basic
##    print(create_parks_list_of_lists(split_string("this;is;a;new;line;\nthis;is;a;new;line;\ntest")))
##    print(create_parks_list_of_lists(split_string(read_url(PARKS_URL)))[0])
    #test create_parks_list_of_lists -- TypeError
##    print(create_parks_list_of_lists("this;is;a;new;line;"))

    #test find_index_number -- basic
##    print(find_index_number(TEST_PARK_DATA, "Name"))
    #test find_index_number -- TypeError -- 1st parameter
##    print(find_index_number("TEST_PARK_DATA", "Name"))
    #test find_index_number -- TypeError -- 2nd parameter
##    print(find_index_number(TEST_PARK_DATA, ["Name"]))

    #test create_list_of_park_objects -- basic
##    test_list_park_objects = create_list_of_park_objects(TEST_PARK_DATA)
##    print(test_list_park_objects[0].name)
    #test create_list_of_park_objects -- TypeError
##    test_list_park_objects = create_list_of_park_objects("TEST_PARK_DATA")

    #test get_neighbourhood_name_data -- basic
##    test_nbh_list = get_neighbourhood_name_data(split_string(read_url(CENSUS_URL)))
##    print(test_nbh_list[0])
    #test get_neighbourhood_name_data -- TypeError
##    test_nbh_list = get_neighbourhood_name_data(read_url(CENSUS_URL))

    #test get_total_population_data -- basic
##    test_ppl_list = get_total_population_data(split_string(read_url(CENSUS_URL)))
##    print(test_ppl_list[0])
    #test get_total_population_data -- TypeError
##    test_ppl_list = get_total_population_data(read_url(CENSUS_URL))

    #test create_list_of_neighbourhood_objects -- basic
##    test_list_nbh_objects = create_list_of_neighbourhood_objects(TEST_NEIGHBOURHOOD_NAME, TEST_POPULATION_LIST)
##    print(test_list_nbh_objects[0].name, test_list_nbh_objects[1].population)
    #test create_list_of_neighbourhood_objects -- TypeError
##    test_list_nbh_objects = create_list_of_neighbourhood_objects("TEST_NEIGHBOURHOOD_NAME", TEST_POPULATION_LIST)
##    test_list_nbh_objects = create_list_of_neighbourhood_objects(TEST_NEIGHBOURHOOD_NAME, "TEST_POPULATION_LIST")
    #test create_list_of_neighbourhood_objects -- ValueError -- non-associated lists
##    test_list_nbh_objects = create_list_of_neighbourhood_objects(TEST_NEIGHBOURHOOD_NAME[1::], TEST_POPULATION_LIST)

    #test add_parks_to_neighbourhoods -- basic  
    park1 = Park("A Park", "Downtown", 3.2)
    park2 = Park("B Park", "West End", 5.0)
    park3 = Park("C Park", "Downtown", 6.0)
    park4 = Park("D Park", "West End", 2.8)
    park5 = Park("E Park", "West End", 7.1)
    park6 = Park("F Park", "Downtown", 2.3)
    test_list_park_objects = [park1, park2, park3, park4, park5, park6]
    test_list_nbh_objects = create_list_of_neighbourhood_objects(TEST_NEIGHBOURHOOD_NAME, TEST_POPULATION_LIST)
##    add_parks_to_neighbourhoods(test_list_park_objects, test_list_nbh_objects)
##    print(test_list_nbh_objects[1].parks[0].name)
    #test add_parks_to_neighbourhoods -- TypeError -- parameters
##    add_parks_to_neighbourhoods("test_list_park_objects", test_list_nbh_objects)
##    add_parks_to_neighbourhoods(test_list_park_objects, "test_list_nbh_objects")
    #test add_parks_to_neighbourhoods -- TypeError -- objects
##    add_parks_to_neighbourhoods(test_list_park_objects, test_list_park_objects)

    #test analyze_park_data_of_neighbourhoods -- basic
##    add_parks_to_neighbourhoods(test_list_park_objects, test_list_nbh_objects)
##    analyze_park_data_of_neighbourhoods(test_list_nbh_objects)
##    print(test_list_nbh_objects[1].parks_num)
##    print(test_list_nbh_objects[1].area_person_sqm)
    #test add_parks_to_neighbourhoods -- TypeError -- parameters
##    analyze_park_data_of_neighbourhoods("test_list_nbh_objects")
    #test add_parks_to_neighbourhoods -- TypeError -- objects
##    analyze_park_data_of_neighbourhoods(test_list_park_objects)

    
if __name__ == "__main__":
    main()
