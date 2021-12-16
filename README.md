# Dynamic-Traffic-Lights-Simulation

To run the Jupyter Notebooks of this project click here --> [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcostfermin/Dynamic-Traffic-Lights-Simulation/main) (COMING SOON)

The following capstone simulation project was done as a partial requirement to obtain the Bachelor of Engineering in Electrical Engineering from The City College of New York under the supervision of Prof. Dr. Mohamed Ali. 

This project aims to create a traffic simulation where the Traffic Lights are dynamically controled based on the traffic density at a given intersection reducing congestion. The performance of three techonologies (High Speed Camera, PIR Sensor, and Smart Antenna) were compared to determine which technology is more efficient at reducing traffic congestion by focusing on the Average Waiting Time and Total Number of Cars Served at the intersection.

# Simulations

# Antenna

This module simulates the Dynamic Traffic Lights with a smart antenna covering the intersection. The fundamental assumption for the smart antenna techonology is to provide a highly efficient method to dynamically control traffic lights by exploiting the capabilities of the telecominications antennas currently in use by mobile carriers. It determines the number of cars present in each direction of the intersection by summing the number of vehicles East to West and North to South that collide with each lane of the intersection.

The green light timing of each traffic light ranges from 60 to 180 seconds depending on the number of cars present. The antenna will verify the presence of vehicles in either direction every 60 seconds. If there are cars present in the opposite direction, the light will switch. In case there is no traffic in either direction the green lights will stay on for 180 seconds to then switch to the opposite direction, so on and so forth.

![Antenna](https://user-images.githubusercontent.com/90121492/146289025-dd46484e-732a-42ef-9cba-36bbc42d0081.PNG)

# Camera

This module simulates the Dynamic Traffic Lights with a high speed camera in each direction. The fundamental assumption for the high speed camera techonology is to provide a highly efficient image processing method to dynamically control traffic lights by detecting the presence of vehicles at the intersection. In a real-time IoT project the cameras would be connected to a image processing module that detects the vehicles using computer vision. However, for this simulation, only the expected behavior of the traffic lights after image processing was considered.

This module assumes that the cameras are sending their live feed to a image processing unit, and the traffic lights' timing self-adjust based on the processing done by this unit. The green light timing of each traffic light changes dynamically by providing a longer greentime to the direction that has the most vehicles. The signals are activated in a clock-wise direction.

![Camera](https://user-images.githubusercontent.com/90121492/146289019-aabf0f51-2d58-45b8-91b8-55c988c145c7.PNG)

# PIR Sensor

This module simulates the Dynamic Traffic Lights with PIR Sensors at the intersection. The fundamental assumption for the PIR Sensor techonology is to provide a method of detecting the presence of cars based on movement in each direction of the intersecion. In this simulation, the PIR sensors are represented by "rays" that detect the presence of vehicles when they "collide" with the rays within the sensors' operating range.

The PIR sensor logic is implemented following a "master-slave" module where East is lane 0, West is lane 2, North is lane 1 and South is lane 3. With this assumption the sensors check every greenmax if vehicles are present in the opposite direction.

![PIRsensor](https://user-images.githubusercontent.com/90121492/146289029-65cffae3-6111-4c63-a9e9-ba3670efd4dd.PNG)

# Data

At the end of the simulation the algorithm will print the number of cars served per techonology, the average waiting time in red at the intersection, and their efficiencies compared to each other in the form of graphs and tables.

For reference, a short simulation time (1 hour) was run for each technology, and the results were as seen below:  

![VehiclesServed_vs_Traffictechnology](https://user-images.githubusercontent.com/90121492/146331577-6da27cad-593f-44f8-9df7-2a86ddddf1bc.png)

![AWT_vs_TrafficTechnology](https://user-images.githubusercontent.com/90121492/146331602-97867368-d7ec-4f82-914c-39982bd18cda.png)

![CarsServed_vs_Servicedirection](https://user-images.githubusercontent.com/90121492/146332527-ccd20d29-db46-4287-baca-53a502cc47a8.png)

![Tables](https://user-images.githubusercontent.com/90121492/146331623-0069070e-9bd9-490e-9ad7-7725a9a59bc4.PNG)
