"""
Author: Pedro Breton pab3507@rit.edu
Date: 11/14/2017
This task involves looking at how region and income affect life expectancy.
Turtle graphics is used to generate plots to visualize the data.
"""
from utils import *
import turtle as t


def initialize_screen(screen_size):
    """
    Initialize the screen for the graph
    Args:
        screen_size: int

    Returns:
    """

    t.setworldcoordinates(0, 0, screen_size, screen_size)
    t.left(90)
    t.up()



def draw_skeleton():
    """
    Draw the skeleton of the graph
    Returns:

    """
    t.goto(10, 10)
    t.down()
    t.forward(80)
    t.up()
    t.goto(10, 10)
    t.down()
    t.right(90)
    t.forward(80)
    t.up()
    t.left(90)
    t.goto(8, 10)

    for i in range(10):
        t.write(str(i * 10), font=("Arial", 12, "normal"))
        t.forward(8.5)

    t.goto(1, 50)
    t.write("Life\nExp.", font=("Arial", 12, "normal"))

    t.goto(10, 6)
    t.write("1960", font=("Arial", 12, "normal"))

    t.goto(87, 6)
    t.write("2015", font=("Arial", 12, "normal"))

    t.goto(48, 3)
    t.write("Year", font=("Arial", 12, "normal"))


def draw_legend_income():
    """
    Low Income --> Blue
    Upper Middle Income --> Red
    Lower Middle Income --> Green
    High Income --> Orange
    Returns: colors
    """

    colors = {"Low income": "blue", "Upper middle income": "red", "Lower middle income": "green",
              "High income": "orange"}

    initial_y = 96

    for key, value in colors.items():
        t.goto(14, initial_y)
        t.pencolor(value)
        t.write("%s ------------" % key, font=("Arial", 12, "normal"))
        initial_y -= 3

    t.pencolor("black")

    return colors


def draw_legend_region():
    """
    Sub-Saharan Africa --> Blue
    South Asia --> Red
    Europe & Central Asia --> Green
    Latin America & Caribbean --> Orange
    Middle East & North Africa --> Black
    North America --> Yellow
    East Asia & Pacific --> purple
    Returns: colors
    """

    colors = {"Sub-Saharan Africa": "blue", "South Asia": "red", "Europe & Central Asia": "green",
              "Latin America & Caribbean": "orange", "Middle East & North Africa": "black", "North America": "yellow",
              "East Asia & Pacific": "purple"}

    initial_y = 97

    for key, value in colors.items():
        t.goto(14, initial_y)
        t.pencolor(value)
        t.write("%s ------------" % key, font=("Arial", 12, "normal"))
        initial_y -= 3

    t.pencolor("black")

    return colors


def get_median_life_expectancy(data, year):
    """
    Return the median life expectancy of a particular year
    Args:
        data: a tuple with two dictionaries
        year: int target year

    Returns: float median life expectancy

    """
    values_year = []
    data = filter_year(data[0], data[1])

    for value in data.values():
        if value.values[year - 1960][1] != 0:
            values_year.append(value.values[year - 1960])

    values_year = sorted(values_year, key=lambda x: x[1])

    if len(values_year) % 2 == 1:

        return values_year[len(values_year) // 2][1]
    else:
        return (values_year[len(values_year) // 2][1] + values_year[len(values_year) // 2 - 1][1]) / 2


def make_lines(data, colors, type):
    """
    plots the line of the graph
    Args:
        data: dictionary
        colors: dictionary
        type: string

    Returns:

    """
    for key, value in colors.items():
        if type == "income":
            sub_data = filter_income(data, key)
        elif type == "region":
            sub_data = filter_region(data, key)

        t.pencolor(value)

        for year in range(1960, 2016):
            y = get_median_life_expectancy(sub_data, year)
            x = year - 1960

            x = 10 + (80 / len(range(1960, 2016)) * x)
            t.pensize(4)
            t.goto(x, y)
            t.down()

        t.up()


def main():
    data = read_data("worldbank_life_expectancy")

    initialize_screen(100)
    draw_skeleton()
    make_lines(data, draw_legend_income(), "income")

    while input("Press enter to continue...") != "":
        pass

    t.reset()

    initialize_screen(100)
    draw_skeleton()
    make_lines(data, draw_legend_region(), "region")
    t.done()


if __name__ == '__main__':
    main()
