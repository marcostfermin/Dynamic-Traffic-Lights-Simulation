"""
@author: Marcos Tulio Fermin Lopez
"""

import Data_Manager
import matplotlib.pyplot as plt

import Tables
import tables  # for making the table

""" This module contains the functions that generate the plots.
"""


def plot_AWT():
    # creating the dataset
    data = Data_Manager.get_data()

    font = {'family': 'serif',  # you can change the font here or remove fontdict = font in lin 31,32,33 and it'll type in the default font!
            'color': 'black',
            'weight': 'normal',
            'size': 16,
            }

    keys = list(data.keys())
    print('Techs: ', keys)
    values = []

    for i in keys:
        val = int(data[i]['AWT'])  # convert to int
        values.append(val)

    print('Average Waiting Time (AWT):', values)

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(keys, values, color='maroon', width=0.5)

    plt.xlabel("Traffic Technology", fontdict=font)
    plt.ylabel("Average Waiting Time", fontdict=font)
    plt.title("Comparison of Average Waiting Time", fontdict=font)
    plt.grid(True)
    plt.show()


def plot_Antenna():
    # creating the dataset
    data = Data_Manager.get_data()

    font = {'family': 'serif',  # you can change the font here or remove fontdict = font in lin 31,32,33 and it'll type in the default font!
            'color': 'black',
            'weight': 'normal',
            'size': 16,
            }

    keys = list(data.keys())
    print('Techs: ', keys)
    values = []
    EW = int(data['Antenna']['EastToWest'])  # convert to int
    NS = int(data['Antenna']['NorthToSouth'])  # convert to int

    keys = ['East-West', 'North-South']
    values = [EW, NS]

    print('Cars Served East-West & North-South:', values)

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(keys, values, color='maroon', width=0.5)

    plt.xlabel("Service Direction", fontdict=font)
    plt.ylabel("Cars Served", fontdict=font)
    plt.title("Cars Served by Antenna in East-West and North-South Direction", fontdict=font)
    plt.grid(True)
    plt.show()


def show_graph():
    # creating the dataset
    data = Data_Manager.get_data()

    font = {'family': 'serif',  # you can change the font here or remove fontdict = font in lin 31,32,33 and it'll type in the default font!
            'color': 'black',
            'weight': 'normal',
            'size': 16,
            }

    keys = list(data.keys())
    print('Techs: ', keys)
    values = []

    for i in keys:
        val = int(data[i]['carsServiced'])  # convert to int
        values.append(val)

    print('Cars Serviced:', values)

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(keys, values, color='maroon', width=0.5)

    plt.xlabel("Traffic Technology", fontdict=font)
    plt.ylabel("No. of Vehicles Serviced", fontdict=font)
    plt.title("Vehicles Serviced Based on Traffic Management Technology", fontdict=font)
    plt.grid(True)
    plt.show()


def plot_all():  # Plots all graphs
    show_graph()
    plot_AWT()
    plot_Antenna()
    Tables.show_AWT_Table()


if __name__ == "__main__":
    plot_all()
   # plot_all()
