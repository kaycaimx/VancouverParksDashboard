'''
    Kay (Mengxian) Cai
    CS5001, Fall 2022
    Data Dashboard Final Project - Milestone 2
    functions_file.py -- store all functions for the driver
'''
import requests
import pandas
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from park import Park
from neighbourhood import Neighbourhood

PARK_HEADER_INDEX = 0#index number of the header row in the parks data list split from parks.csv by new line,
#the headers are "ParkID;Name;Official;Advisories;SpecialFeatures;Facilities;Washrooms;StreetNumber;..."
PARK_CONTENT_INDEX = 1#index number where the real data of each park starts in the parks data list split from
#parks.csv by new line
NEIGHBOURHOOD_NAME_INDEX = 4#index number of the name of all neighbourhoods in the list split from the
#CensusLocalAreaProfiles2016.csv by new line, this item will be further split by "," to get name of each neighbourhood 
TOTAL_POPULATION_INDEX = 5#index number of the total population of each neighbourhood in the list split from the
#CensusLocalAreaProfiles2016.csv by new line, this item will be further split by ","" to get population of each neighbourhood 
NEIGHBOURHOOD_NAME_START_INDEX = 2#index number where the real data of each neighbourhood's name start in the abovementioned
#list split by ","
TOTAL_POPULATION_START_INDEX = 1#index number where the real data of each neighbourhood's population start in the abovementioned
#list split by ",""
NEIGHBOURHOODS_NUMBER = 22#total number of neighbourhoods in Vancouver
CENSUS_JUNK_CHARACTERS = ["\"", ","]
ALPHABETICAL_INDEX = 0#index of alphabetical sorting order in GUI
ASCENDING_INDEX = 1#index of ascending sorting order in GUI
DESCENDING_INDEX = 2#index of descending sorting order in GUI
PAPP_ASCENDING_INDEX = 3#index of ascending sorting order (per person park area) in GUI
PAPP_DESCENDING_INDEX = 4#index of descending sorting order (per person park area) in GUI


def read_url(url_address):
    '''
    Function -- read_url
        purpose: to get content from a web and convert it to a string.
    Parameters:
        url_address -- a string, which should be a valid url address
    Return:
        a string which is the content of the file
    Raise errors:
        TypeError if the url is not passed as a string
        ValueError if the url address does not start with "https://"
        ConnectionError, HTTPError, and RequestError for request exceptions
    '''
    if not isinstance(url_address, str):
        raise TypeError ("This function only takes a string.")
    if url_address[0:8] != "https://":
        raise ValueError ("This is not a valid secure url address.")
    try:
        response = requests.get(url_address)
        content = response.text
        return content
    except requests.ConnectionError as connect_err:
        raise connect_err
    except requests.HTTPError as http_err:
        raise http_err
    except requests.RequestException as request_err:
        raise request_err


def split_string(string_input):
    '''
    Function -- split_string
        purpose: to split a string by new line to a list.
    Parameters:
        string_input -- a string to be split
    Return:
        a list contains the string split by new line
    Raise errors:
        TypeError if the parameter is not a string
    '''
    if not isinstance(string_input, str):
        raise TypeError ("This function only takes a string.")
    new_list = string_input.split("\n")
    return new_list


def create_parks_list_of_lists(list_input):
    '''
    Function -- create_parks_list_of_lists
        purpose: to convert a list of strings into a list of lists, where each nested
        list is a list of data of each park split by ";" from each string item, all
        nested lists are associated.
    Parameters:
        list_input -- a list, which contains data converted from the csv string file
    Return:
        a list of lists as described above
    Raise errors:
        TypeError if the parameter is not a list of strings
    '''
    if not isinstance(list_input, list):
        raise TypeError ("This function only takes a list.")
    list_of_lists = []
    for i in range(len(list_input)):
        if not isinstance(list_input[i], str):
            raise TypeError ("This function only takes a list of strings.")
        else:
            if list_input[i] != "":
                nested_list = list_input[i].split(";")
                list_of_lists.append(nested_list)
    return list_of_lists


def find_index_number(parks_data_list, header_name):
    '''
    Function -- find_index_number
        purpose: to find the index number of a specified data according to the name
        of such specified data in the header list item, so this index number can be
        used to get this type of data for all the parks in the list of lists since
        they are associated.
    Parameters:
        parks_data_list -- a list of lists, where the first item is the header list
        and each following nested list is a list of data of each park
    Return:
        an integer, which represents the index number of the specified data
    Raise errors:
        TypeError if the first parameter is not a list or the second parameter is not a
        string
    '''
    if not isinstance(parks_data_list, list):
        raise TypeError ("The first parameter must be a list.")
    if not isinstance(header_name, str):
        raise TypeError ("The second parameter must be a string.")
    index_num = parks_data_list[PARK_HEADER_INDEX].index(header_name)
    return index_num

    
def create_list_of_park_objects(parks_data_list):
    '''
    Function -- create_list_of_park_objects
        purpose: to create a list of Park instances and store data from the list of
        parks' data list into those instances.
    Parameters:
        parks_data_list -- a list of lists, where the first item is the header list
        and each following nested list is a list of data of each park
    Return:
        a list of Park instances as described above
    Raise errors:
        TypeError if the parameter is not a list
    '''
    if not isinstance(parks_data_list, list):
        raise TypeError ("This function only takes a specified list.")
    name_index = find_index_number(parks_data_list, "Name")
    neighbour_index = find_index_number(parks_data_list, "NeighbourhoodName")
    hectare_index = find_index_number(parks_data_list, "Hectare")
    list_of_parks_objects = []
    for i in range(PARK_CONTENT_INDEX, len(parks_data_list)):
        park_instance = Park(parks_data_list[i][name_index], parks_data_list[i][neighbour_index], \
                             float(parks_data_list[i][hectare_index]))
        list_of_parks_objects.append(park_instance)
    return list_of_parks_objects


def get_neighbourhood_name_data(census_list):
    '''
    Function -- get_neighbourhood_name_data
        purpose: to clean and parse the list of strings converted from the census local
        data csv file, get the names of all 22 neighbourhoods and store them into a list.
    Parameters:
        census_list -- a list of strings, which is converted from the census local data
        csv file
    Return:
        a list of 22 strings, which are names of 22 neighbourhoods in Vancouver
    Raise errors:
        TypeError if the parameter is not a list
    '''
    if not isinstance(census_list, list):
        raise TypeError("This function only takes a list.")
    nbh_initial_list = census_list[NEIGHBOURHOOD_NAME_INDEX].split(",")
    nhb_name_list = []
    for i in range(NEIGHBOURHOOD_NAME_START_INDEX, NEIGHBOURHOOD_NAME_START_INDEX + NEIGHBOURHOODS_NUMBER):
        clean_name = nbh_initial_list[i].strip()
        nhb_name_list.append(clean_name)
    return nhb_name_list


def get_total_population_data(census_list):
    '''
    Function -- get_total_population_data
        purpose: to clean and parse the list of strings converted from the census local
        data csv file, get the total population data of all 22 neighbourhoods and store
        them into a list.
    Parameters:
        census_list -- a list of strings, which is converted from the census local data
        csv file
    Return:
        a list of 22 integers, each of which is the total population of the corresponding
        neighbourhood, this list is associated with the list of names of neighbourhoods
    Raise errors:
        TypeError if the parameter is not a list
    '''
    if not isinstance(census_list, list):
        raise TypeError ("This function only takes a list.")
    ttl_ppl_initial_list = census_list[TOTAL_POPULATION_INDEX].split(",\"")
    ttl_ppl_list = []
    for i in range(TOTAL_POPULATION_START_INDEX, TOTAL_POPULATION_START_INDEX + NEIGHBOURHOODS_NUMBER):
        clean_string = ttl_ppl_initial_list[i].strip()
        for junkchara in CENSUS_JUNK_CHARACTERS:        
            clean_string = clean_string.replace(junkchara, "")
        clean_number = int(clean_string)
        ttl_ppl_list.append(clean_number)
    return ttl_ppl_list
    

def create_list_of_neighbourhood_objects(name_list, population_list):
    '''
    Function -- create_list_of_neighbourhood_objects
        purpose: to create a list of Neighbourhood instances and store data from the
        population list into those instances.
    Parameters:
        name_list -- a list of 22 strings, which are names of 22 neighbourhoods in Vancouver
        population_list -- a list of 22 integers, each of which is the total population of
        the corresponding neighbourhood
        These two lists are associated
    Return:
        a list of Neighbourhood instances as described above
    Raise errors:
        TypeError if either parameter is not a list
        ValueError if the two lists are not associated
    '''
    if not isinstance(name_list, list):
        raise TypeError ("The first parameter should be a list.")
    if not isinstance(population_list, list):
        raise TypeError ("The second parameter should be a list.")
    if len(name_list) != len(population_list):
        raise ValueError("The two lists are not associated.")
    list_of_nbh_objects = []
    for i in range(len(name_list)):
        nbh_instance = Neighbourhood(name_list[i], population_list[i])
        list_of_nbh_objects.append(nbh_instance)
    return list_of_nbh_objects
    
    
def add_parks_to_neighbourhoods(parks_list, neighbourhoods_list):
    '''
    Function -- add_parks_to_neighbourhoods
        purpose: to add all Park instances in the list of Park objects to their respective
        Neighbourhood by matching the location of Park with name of Neighbourhood.
    Parameters:
        parks_list -- a list of Park instances, which includes all parks in Vancouver
        neighbourhoods_list -- a list of 22 Neighbourhood instances
    Return:
        None
    Raise errors:
        TypeError if either parameter is not a list
        TypeError if list of wrong instances given
    '''
    if not isinstance(parks_list, list):
        raise TypeError ("The first parameter should be a list.")
    if not isinstance(neighbourhoods_list, list):
        raise TypeError ("The second parameter should be a list.")
    for i in range(len(parks_list)):
        try:
            for j in range(len(neighbourhoods_list)):
                if not isinstance(neighbourhoods_list[j], Neighbourhood):
                    raise TypeError("This function only takes a list of Neighbourhood instances.")
                else:
                    if parks_list[i].location == neighbourhoods_list[j].name:
                        neighbourhoods_list[j].add_park(parks_list[i])
        except TypeError as type_err:
            raise type_err
        except ValueError as value_err:
            raise value_err
            

def analyze_park_data_of_neighbourhoods(neighbourhoods_list):
    '''
    Function -- analyze_park_data_of_neighbourhoods
        purpose: to analyze park related data of all Neighbourhoods by counting total number of
        Parks and calculating the park area per person.
    Parameters:
        neighbourhoods_list -- a list of 22 Neighbourhood instances
    Return:
        None
    Raise errors:
        TypeError if not a list or list of wrong instances given
    '''
    if not isinstance(neighbourhoods_list, list):
        raise TypeError ("The parameter should be a list.")
    for j in range(len(neighbourhoods_list)):
        if not isinstance(neighbourhoods_list[j], Neighbourhood):
            raise TypeError("This function only takes a list of Neighbourhood instances.")
        else:
            neighbourhoods_list[j].count_parks()
            neighbourhoods_list[j].calculate_parks_area_per_person_sqm()


def make_neighbourhoods_data_frame_and_graph(neighbourhoods_list, choice_index, title):
    '''
    Function -- make_neighbourhoods_data_frame_and_graph
        purpose: to make a data frame containing certain park related data of all
        Neighbourhoods (including total number of parks and park area per person) and
        make a bar graph from such data frame.
    Parameters:
        neighbourhoods_list -- a list of 22 Neighbourhood instances
        choice_index -- an integer from 0 to 4, which represents sorting orders: alphabetical,
        ascending or descending (each in terms of parks number and per person area)
        title -- a string, which is the title of the graph to be made
    Return:
        None
    Raise errors:
        TypeError if not a list or list of wrong instances given
    '''
    if not isinstance(neighbourhoods_list, list):
        raise TypeError ("The parameter should be a list.")
    nbh_copy = []
    for nbh in neighbourhoods_list:
        if not isinstance(nbh, Neighbourhood):
            raise TypeError("This function only takes a list of Neighbourhood instances.")
        else:
            nbh_copy.append(nbh)
    nbh_len = len(nbh_copy)
    #sorting the order of neighbourhood instances according to the choice_index
    if choice_index == ASCENDING_INDEX:
        for i in range(1, nbh_len):
            current = nbh_copy[i]
            j = i - 1
            while j >= 0 and nbh_copy[j].parks_num > current.parks_num:
                nbh_copy[j + 1] = nbh_copy[j]
                nbh_copy[j] = current
                j -= 1       
    if choice_index == DESCENDING_INDEX:
        for i in range(1, nbh_len):
            current = nbh_copy[i]
            j = i - 1
            while j >= 0 and nbh_copy[j].parks_num < current.parks_num:
                nbh_copy[j + 1] = nbh_copy[j]
                nbh_copy[j] = current
                j -= 1
    if choice_index == PAPP_ASCENDING_INDEX:
        for i in range(1, nbh_len):
            current = nbh_copy[i]
            j = i - 1
            while j >= 0 and nbh_copy[j].area_person_sqm > current.area_person_sqm:
                nbh_copy[j + 1] = nbh_copy[j]
                nbh_copy[j] = current
                j -= 1
    if choice_index == PAPP_DESCENDING_INDEX:
        for i in range(1, nbh_len):
            current = nbh_copy[i]
            j = i - 1
            while j >= 0 and nbh_copy[j].area_person_sqm < current.area_person_sqm:
                nbh_copy[j + 1] = nbh_copy[j]
                nbh_copy[j] = current
                j -= 1
    #make data frame from the sorted list of neighbourhood instances
    name_list = []
    parks_num_list = []
    park_area_person = []
    for i in range(nbh_len):
        name_list.append(nbh_copy[i].name)
        parks_num_list.append(nbh_copy[i].parks_num)
        park_area_person.append(nbh_copy[i].area_person_sqm)
    data = (name_list, parks_num_list, park_area_person)
    dashboard_labels = ("Neighbourhood Name", "Parks Number", "PerPerson Area(sqm)")
    nbh_dictionary = dict(zip(dashboard_labels, data))
    df1 = pandas.DataFrame(nbh_dictionary)
    #draw figure from the data frame
    figure1, ax1 = plt.subplots()
    figure1.set_figwidth(8.4)
    figure1.set_figheight(6.3)
    ax1.set_title(title)
    ax1.set_ylabel("Number of Parks")
    df1.plot(kind="bar", color=["salmon", "teal"], secondary_y ="PerPerson Area(sqm)", legend=False, ax=ax1)
    ax1.right_ax.set_ylabel("Park Area Per Person (sqm)")
    xticklabels = list(df1["Neighbourhood Name"])
    ax1.set_xticklabels(xticklabels)
    parknum = mpatches.Patch(color="salmon", label="Parks Number")
    papp = mpatches.Patch(color="teal", label="PerPerson Area (sqm)")
    plt.legend(handles=[parknum, papp], loc="upper center")
    figure1.autofmt_xdate()
    plt.tight_layout()
    plt.savefig(title+".png")
    

def make_bar_graph_from_dict(nbh_list, nbh_index, sort_index):
    '''
    Function -- make_bar_graph_from_dict
        purpose: to make a bar graph from a dictionary where the keys are the names of parks
        and values are areas of parks in a chosen Neighbourhood.
    Parameters:
        nbh_list -- a list of Neighbourhood instances, each Neighbourhood contains relevant
        data of parks located in such Neighbourhood
        nbh_index -- an integer from 0 to 21, which represents the index number of the chosen
        Neighbourhood in the list of Neighbourhood instances
        sort_index -- an integer from 0 to 2, which represents sorting orders: alphabetical,
        ascending or descending
    Return:
        None
    Raise errors:
        TypeError if any incorrect parametere is given
        messagebox if nbh_index or sort_index is not chosen
    '''
    if not isinstance(nbh_list, list):
        raise TypeError("The first parameter must be a list of Neighbourhood instances.")
    if not isinstance(nbh_index, int) or not isinstance(sort_index, int):
        raise TypeError("The second and third parameters must be integers.")
    if nbh_index != -1 and sort_index != -1:
        nbh_dict = {}
        nbh = nbh_list[nbh_index]
        if sort_index == ALPHABETICAL_INDEX:
            nbh.sort_parks_alphabetically()
        elif sort_index == ASCENDING_INDEX:
            nbh.sort_parks_area_ascendingly()
        else:
            nbh.sort_parks_area_descendingly()
        for park in nbh.parks:
            nbh_dict[park.name] = park.area
        plt.clf()
        plt.bar(range(len(nbh_dict)), list(nbh_dict.values()), color="teal", align='center')
        plt.xticks(range(len(nbh_dict)), list(nbh_dict.keys()))
        plt.title(nbh.name)
        plt.ylabel("Park Area (hectare)")
        plt.gcf().autofmt_xdate()
        plt.show()
    else:
        messagebox.showinfo(title = "Reminder!", message = 'You haven\'t chosen Neighbourhood and/or sorting order.')
