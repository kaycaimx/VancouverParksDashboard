'''
    Kay (Mengxian) Cai
    CS5001, Fall 2022
    Data Dashboard Final Project - Milestone 2
    data_dashboard.py -- driver
'''
import requests
from park import Park
from neighbourhood import Neighbourhood
from park_avai_gui import ParkAvaiGui
from functions_file import *
from tkinter import *
from tkinter import ttk

#data sets to be used:
PARKS_URL = "https://opendata.vancouver.ca/explore/dataset/parks/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
CENSUS_URL = "https://webtransfer.vancouver.ca/opendata/csv/CensusLocalAreaProfiles2016.csv"

TITLE = "Park Availability of Vancouver Neighbhourhoods"

def main():
    try:
        #download, clean and parse parks data into a list of Park objects
        parks_data_list = create_parks_list_of_lists(split_string(read_url(PARKS_URL)))
        park_objects_list = create_list_of_park_objects(parks_data_list)

        #download, clean and parse census local data into a list of Neighbourhood objects
        census_data_list = split_string(read_url(CENSUS_URL))
        neighbourhood_name_list = get_neighbourhood_name_data(census_data_list)
        population_list = get_total_population_data(census_data_list)
        neighbourhood_objects_list = create_list_of_neighbourhood_objects(neighbourhood_name_list, population_list)

        #assign Park objects to Neighbourhood objects by matching the location of Park
        #with name of Neighbourhood 
        add_parks_to_neighbourhoods(park_objects_list, neighbourhood_objects_list)

        #do an analysis of park data for each Neighbourhood
        analyze_park_data_of_neighbourhoods(neighbourhood_objects_list)

        #GUI for visulization and user interaction
        root = Tk()
        root.title(TITLE)        
        my_gui = ParkAvaiGui(root, TITLE, neighbourhood_name_list, neighbourhood_objects_list)   
        root.mainloop()

    except requests.ConnectionError as connect_err:
        raise connect_err
    except requests.HTTPError as http_err:
        raise http_err
    except requests.RequestException as request_err:
        raise request_err
    except TypeError as type_err:
        raise type_err
    except ValueError as value_err:
        raise value_err
     
if __name__ == "__main__":
    main()
