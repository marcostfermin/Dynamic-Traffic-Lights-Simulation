# Dynamic Traffic Lights Management System Based On Traffic Flow Simulation With Performance Comparison of Various Smart Traffic Lights Technologies

To run the Jupyter Notebooks of this project click here --> [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marcostfermin/Dynamic-Traffic-Lights-Simulation/main) (COMING SOON)

The following capstone simulation project was done as a partial requirement to obtain the Bachelor of Engineering in Electrical Engineering from The City College of New York under the supervision of Prof. Dr. Mohamed Ali. 

This project aims to create a traffic simulation where the Traffic Lights are dynamically controled based on the traffic density at a given intersection reducing congestion. The performance of three techonologies (High Speed Camera, PIR Sensor, and Smart Antenna) were compared to determine which technology is more efficient at reducing traffic congestion by focusing on the Average Waiting Time and Total Number of Cars Served at the intersection.

# Graphical User Interface

![GUI_1](https://user-images.githubusercontent.com/90121492/146970626-5b3b7249-6777-42b8-85d8-9531843e7ee7.PNG)

![GUI_2](https://user-images.githubusercontent.com/90121492/146970640-d3e4c3ba-2f74-4b16-80f7-02d40aea1522.PNG)

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

# References 

[1] J. Jin, X. Ma, and I. Kosonen, “An intelligent control system for traffic lights with simulation-based evaluation,” Control Engineering Practice, vol. 58, pp. 24–33, 2017.

[2] A. Joyo, R. Yaqub, and N. Madamopoulos, “Intelligent traffic-lights management by exploiting smart antenna technology (itsat),” IEEE Intelligent Transportation Systems Magazine, pp. 1–11, 2020.

[3] R. Yaqub, A. Joyo, K. Heidary, and N. Madamopoulos, “Green-initiative for realizing adaptive traffic-signals by exploiting smart-antenna technology (greatest),” IEEE Intelligent Transportation Systems Magazine, vol. 12, no. 4, pp. 66–77, 2020.

[4] M. A. Kamran, H. Ramezani, S. Masoumzadeh, and F. Nikkhoo, “Traffic light signal timing using simulation,” Communications on Advanced Computational Science with Applications, vol. 1, pp. 1–11, 2017.

[5] B. Wee, J. Annema, and D. Banister, The transport system and transport policy: an introduction. Jan. 2013, p. 399, isbn: 9781781952047.

[6] N. Gartner and D. Hou, “Comparative evaluation of alternative traffic control strategies,” Transportation Research Record Journal of the Transportation Research Board, vol. 1360, pp. 66–73, Dec. 1992.

[7] K. Salimifard and M. Ansari, “Modeling and simulation of urban traffic signals,” International Journal of Modeling and Optimization, pp. 172–175, 2013.

[8] E. Lieberman, A. K. Rathi, N. Gartner, and C. Messer, “Revised monograph on traffic flow theory,” U.S. Department of Transportation - Federal Highway Administration, vol. 1, pp. 1–25, 2001.

[9] T. R. Board, E. National Academies of Sciences, and Medicine, Signal Timing Manual - Second Edition, T. Urbanik et al., Eds. Washington, DC: The National Academies Press, 2015. doi: 10.17226/22097. [Online]. Available: https://www.nap.edu/catalog/22097/signal-timing-manual-second-edition.

[10] M. F. Rachmadi et al., “Adaptive traffic signal control system using camera sensor and embedded system,” TENCON 2011 - 2011 IEEE Region 10 Conference, pp. 1261–1265, 2011.

[11] B. Zachariah, P. Ayuba, and L. P. Damuut, “Optimization of traffic light control system of an intersection using fuzzy inference system,” Science World Journal, vol. 12, no. 4, 2017.
