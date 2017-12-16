"""
Author: Pedro Breton pab3507@rit.edu
Date: 11/14/2017
This task involves writing tools for reading and processing the data, as well
as defining data structures to store the data. The other tasks import and use these
tools.
"""
# import modules
from rit_lib import *

# create structs
MainData = struct_type("MainData", (str, 'code'), (list, 'values'))
MetaData = struct_type("Metadata", (str, 'country'), (str, 'region'), (str, 'income'))
CountryValue = struct_type("CountryValue", (str, 'country'), (float, 'value'))
Range = struct_type("Range", (str, 'country'), (int, 'year1'), (int, 'year2'), (float, 'value1'), (float, 'value2'))


def read_data(filename):
    """
    Reads and processes a .txt file
    Args:
        filename: a string, giving the partial name of the data file.

    Returns: a [lst_of_countries] representing the data contained in the data and metadata files
    """
    MainDct = {}  # country -> MainData
    MetaDct = {}  # code -> MetaData
    codeDct = {}  # code -> country
    path = "data/" + filename + "_data.txt"

    with open(path) as data_file:
        data_file.readline()
        for line in data_file:
            data = line.strip().split(",")
            data.pop()
            lst = []
            year = 1960

            for value in data[2:]:
                if value != "":
                    lst.append((year, float(value)))
                else:
                    lst.append((year, 0))
                year += 1
            MainDct[data[0]] = MainData(data[1], lst)
            codeDct[data[1]] = data[0]

    path = "data/" + filename + "_metadata.txt"
    with open(path) as data_file:
        data_file.readline()
        for line in data_file:
            data = line.strip().split(",")
            MetaDct[data[0]] = MetaData(codeDct[data[0]], data[1], data[2])

    return MainDct, MetaDct


def filter_region(data, region):
    """
    If a valid region is entered, the original data is filtered to retain only data corresponding to the specified region.
    If the special string ‘all’ is entered, data for all regions is retained
    If an invalid region is specified, all data is discarded. ("" is considered an invalid region)
    Non-countries are always filtered out
    Args:
        data: represents [one or more data structures (possibly as a tuple)] containing information from the data and metadata files
        region: a string specifying a particular region by which to filter.

    Returns: [One or more data structures] representing data that has been filtered to only retain data corresponding to the specified region
    """
    filtered_dict = {}

    if region != "all":
        for key, info in data[1].items():
            if info.region == region:
                filtered_dict[key] = info

        return (data[0], filtered_dict)
    else:
        return data


def filter_income(data, income):
    """
    If a valid income category is entered, the original data is filtered to retain only data corresponding to the specified income category
    If the special string ‘all’ is entered, data for all income categories is retained
    If an invalid income is specified, all data is discarded. ("" is considered an invalid income)
    Non-countries are always filtered out
    Args:
        data: [The data parameter represents one or more data structures] (possibly as a tuple) containing information from the data and metadata files
        income: a string specifying a particular income category by which to filter.

    Returns: [One or more data structures] representing data that has been filtered to only retain data corresponding to the specified income category
    """
    filtered_dict = {}
    if income != "all":
        for key, info in data[1].items():
            if info.income == income:
                filtered_dict[key] = info

        return (data[0], filtered_dict)
    else:
        return data


def count_countries_in_region(region, MetaDct):
    """
    Returns the amount of countries in a particular region
    Args:
        region: a string
        MetaDct: dictionary with MetaData structs

    Returns: int count of countries in the region

    """
    accum = 0
    for info in MetaDct.values():
        if info.region == region:
            accum += 1
    return accum


def count_countries_in_income_categories(income_region, MetaDct):
    """
    Returns the amount of countries in a particular income category
    Args:
        income_region: a string
        MetaDct: dictionary with MetaData structs

    Returns: int count of countries in the income category

    """
    accum = 0
    for info in MetaDct.values():
        if info.income == income_region:
            accum += 1
    return accum


def filter_year(MainDct, filter):
    """
    filters the countries from MainDct to math those of MetaDct
    Args:
        data: tuple with two dicts

    Returns:a filtered MainDict
    """
    filtered_dict = {}
    for value in filter.values():
        filtered_dict[value.country] = MainDct[value.country]
    return filtered_dict


def main():
    data = read_data("worldbank_life_expectancy")
    MainDct = data[0]
    MetaDct = data[1]

    # print total number of entities
    print("Total number of entities:", len(MainDct))
    counter = 0
    for info in MetaDct.values():
        if info.region != "":
            counter += 1

    # print total number of countries
    print("Total number of countries:", counter)

    # print the total amount of countries per region
    print("Regions and their country count:")
    print("Middle East & North Africa:", count_countries_in_region("Middle East & North Africa", MetaDct))
    print("Europe & Central Asia:", count_countries_in_region("Europe & Central Asia", MetaDct))
    print("North America:", count_countries_in_region("North America", MetaDct))
    print("Latin America & Caribbean:", count_countries_in_region("Latin America & Caribbean", MetaDct))
    print("South Asia:", count_countries_in_region("South Asia", MetaDct))
    print("East Asia & Pacific:", count_countries_in_region("East Asia & Pacific", MetaDct))
    print("Sub-Saharan Africa:", count_countries_in_region("Sub-Saharan Africa", MetaDct))

    # print the total amount of countries per income category
    print("Income categories and their country count")
    print("Lower middle income:", count_countries_in_income_categories("Lower middle income", MetaDct))
    print("Upper middle income:", count_countries_in_income_categories("Upper middle income", MetaDct))
    print("High income:", count_countries_in_income_categories("High income", MetaDct))
    print("Low income:", count_countries_in_income_categories("Low income", MetaDct))

    # print the countries and their codes in a particular region
    target_region = input("Enter region name: ")
    print("Countries in the '%s' region: " % target_region)
    filtered_data = filter_region(data, target_region)
    for key, info in filtered_data[1].items():
        print("%s (%s)" % (info.country, key))

    # print the countries and their codes in a particular income region
    target_income = input("Enter income category: ")
    print("Countries in the '%s' income category: " % target_income)
    filtered_data = filter_income(data, target_income)
    for key, info in filtered_data[1].items():
        print("%s (%s)" % (info.country, key))

    # prints the lif expectancy values associated to a particular country or country code
    # while the input is not an empty string
    while True:
        target_country = input("Enter name of country or country code (Enter to quit): ")
        if target_country == "":
            break
        print("Data for %s:" % target_country)
        counter = 0
        if target_country in MainDct:
            for year in MainDct[target_country].values:
                if year[1] != 0:
                    print("Year: ", year[0], "Life expectancy:", year[1] % (year[0]))
        elif target_country in MetaDct:
            for year in MainDct[MetaDct[target_country].country].values:
                if year[1] != 0:
                    print("Year: ", year[0], "Life expectancy:", year[1] % (year[0]))
        else:
            print("'%s' is not a valid country name or code" % target_country)


if __name__ == '__main__':
    main()
