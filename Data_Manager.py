"""
@author: Marcos Tulio Fermin Lopez
"""

import json
import os.path

""" This module contains all functions used to retrieve the and save the desired data in a .json file.
"""


def get_data():

    # if file exists on disk send it back else send dummy dat to prevent crash

    if os.path.exists("simulation_data.json"):
        with open("simulation_data.json", "r+") as f:  # read
            data = json.load(f)
            return data
    else:
        print(
            "\nThere is so simulation data present on the drive!  --  returning dummy data to prevent crash"
        )
        trafficDataDict = {  # dummy data needed to make the file a template
            "PIR": {"carsServiced": "0", "simulationTime": "0", "AWT": "0"},
            "Camera": {"carsServiced": "0", "simulationTime": "0", "AWT": "0"},
            "Antenna": {
                "carsServiced": "0",
                "EastToWest": "0",
                "NorthToSouth": "0",
                "AWT": "0",
            },
        }
        return trafficDataDict


def make_data_file():

    trafficDataDict = {  # dummy data needed to make the file a template
        "PIR": {"carsServiced": "nil", "simulationTime": "nil", "AWT": "nil"},
        "Camera": {"carsServiced": "nil", "simulationTime": "nil", "AWT": "nil"},
        "Antenna": {
            "carsServiced": "nil",
            "EastToWest": "nil",
            "NorthToSouth": "nil",
            "AWT": "nil",
        },
    }

    # the json file where the output must be stored
    out_file = open("simulation_data.json", "w")

    json.dump(trafficDataDict, out_file, indent=5)

    print("File made")

    out_file.close()


def safely_check_if_file_exists():
    if os.path.exists("simulation_data.json"):
        pass
    else:
        print("Simulation data file is not present\nMaking file . . .")
        make_data_file()


def show_All_Data():

    file = open("simulation_data.json", "r+")

    # returns JSON object as
    # a dictionary
    data = json.load(file)

    # Iterating through the json
    # list
    for i in data:
        print(i, data[i])


def save_Antenna(NorthToSouthCars, EastToWestCars, AWT):

    safely_check_if_file_exists()

    data = get_data()

    with open("simulation_data.json", "w") as f:  # write
        data["Antenna"]["EastToWest"] = EastToWestCars  # left and right
        data["Antenna"]["NorthToSouth"] = NorthToSouthCars  # top and bottom
        data["Antenna"]["AWT"] = AWT
        data["Antenna"]["carsServiced"] = EastToWestCars + NorthToSouthCars

        json.dump(data, f, indent=5)


def save_PIR(carsSeviced, simulationTime, AWT):

    safely_check_if_file_exists()

    data = get_data()

    with open("simulation_data.json", "w") as f:  # write
        data["PIR"]["carsServiced"] = carsSeviced
        data["PIR"]["simulationTime"] = simulationTime
        data["PIR"]["AWT"] = AWT

        json.dump(data, f, indent=5)


def save_Camera(carsSeviced, simulationTime, AWT):

    safely_check_if_file_exists()

    data = get_data()

    with open("simulation_data.json", "w") as f:  # write
        data["Camera"]["carsServiced"] = carsSeviced
        data["Camera"]["simulationTime"] = simulationTime
        data["Camera"]["AWT"] = AWT

        json.dump(data, f, indent=5)


if __name__ == "__main__":

    # save_PIR('1', '1')
    # save_Camera('2', '2')
    # show_All_Data()
    # safely_check_if_file_exists()
    pass
