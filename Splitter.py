"""
@author: Marcos Tulio Fermin Lopez
"""

import os
import Data_Manager
import json


""" This module contains the functions needed to split the data if separate data files are needed.
"""

directoryName = "Individual Simulation Data"  # folder name


def makeFolder():

    if os.path.exists(directoryName):
        pass
    else:
        try:
            os.mkdir(directoryName)
        except OSError:
            print("Creation of the directory failed")
        else:
            print("Successfully created the directory")


def createPIR():
    makeFolder()
    data = Data_Manager.get_data()

    PIR = {  # dummy data needed to make the file a template
        "PIR": {
            "carsServiced": "nil",
            "simulationTime": "nil",
            "AWT": "nil"
        }
    }

    if os.path.exists('Individual Simulation Data/PIR_data.json'):
        with open('Individual Simulation Data/PIR_data.json', 'w') as f:  # read
            PIR['PIR']['carsServiced'] = data['PIR']['carsServiced']
            PIR['PIR']['simulationTime'] = data['PIR']['simulationTime']
            PIR['PIR']['AWT'] = data['PIR']['AWT']

            json.dump(PIR, f, indent=5)
    else:

        # the json file where the output must be stored
        out_file = open("Individual Simulation Data/PIR_data.json", "w")

        if os.path.exists('simulation_data.json'):
            PIR['PIR']['carsServiced'] = data['PIR']['carsServiced']
            PIR['PIR']['simulationTime'] = data['PIR']['simulationTime']
            PIR['PIR']['AWT'] = data['PIR']['AWT']
            json.dump(PIR, out_file, indent=5)

            print('File made')

            out_file.close()

        else:

            json.dump(PIR, out_file, indent=5)

            print('File made')

            out_file.close()


def createCamera():
    makeFolder()
    data = Data_Manager.get_data()

    Camera = {  # dummy data needed to make the file a template
        "Camera": {
            "carsServiced": "0",
            "simulationTime": "0",
            "AWT": "0"
        },
    }

    if os.path.exists('Individual Simulation Data/Camera_data.json'):
        with open('Individual Simulation Data/Camera_data.json', 'w') as f:  # read
            Camera['Camera']['carsServiced'] = data['Camera']['carsServiced']
            Camera['Camera']['simulationTime'] = data['Camera']['simulationTime']
            Camera['Camera']['AWT'] = data['Camera']['AWT']

            json.dump(Camera, f, indent=5)
    else:

        # the json file where the output must be stored
        out_file = open("Individual Simulation Data/Camera_data.json", "w")

        if os.path.exists('simulation_data.json'):
            Camera['Camera']['carsServiced'] = data['Camera']['carsServiced']
            Camera['Camera']['simulationTime'] = data['Camera']['simulationTime']
            Camera['Camera']['AWT'] = data['Camera']['AWT']
            json.dump(Camera, out_file, indent=5)

            print('File made')

            out_file.close()

        else:

            json.dump(Camera, out_file, indent=5)

            print('File made')

            out_file.close()


def createAntenna():
    makeFolder()
    data = Data_Manager.get_data()

    Antenna = {  # dummy data needed to make the file a template
        "Antenna": {
            "carsServiced": "0",
            "EastToWest": "0",
            "NorthToSouth": "0",
            "AWT": "0"
        },
    }

    if os.path.exists('Individual Simulation Data/Antenna_data.json'):
        with open('Individual Simulation Data/Antenna_data.json', 'w') as f:  # read
            Antenna['Antenna']['carsServiced'] = data['Antenna']['carsServiced']
            Antenna['Antenna']['EastToWest'] = data['Antenna']['EastToWest']
            Antenna['Antenna']['NorthToSouth'] = data['Antenna']['NorthToSouth']
            Antenna['Antenna']['AWT'] = data['Antenna']['AWT']

            json.dump(Antenna, f, indent=5)
    else:

        # the json file where the output must be stored
        out_file = open("Individual Simulation Data/Antenna_data.json", "w")

        if os.path.exists('simulation_data.json'):
            Antenna['Antenna']['carsServiced'] = data['Antenna']['carsServiced']
            Antenna['Antenna']['EastToWest'] = data['Antenna']['EastToWest']
            Antenna['Antenna']['NorthToSouth'] = data['Antenna']['NorthToSouth']
            Antenna['Antenna']['AWT'] = data['Antenna']['AWT']
            json.dump(Antenna, out_file, indent=5)

            print('File made')

            out_file.close()

        else:

            json.dump(Antenna, out_file, indent=5)

            print('File made')

            out_file.close()


def splitAll():  # splits all sims into a folder having each individual sim's data separate
    createPIR()

    createCamera()

    createAntenna()


if __name__ == '__main__':
    splitAll()
