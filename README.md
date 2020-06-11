# SDR Receiver Project

![](https://github.com/greenjacketgirl/SDR_Receiver/blob/master/Photos/00000PORTRAIT_00000_BURST20200526190957384.jpg)

**Introduction** | This project was created in the scope of the the class ENGR 357 "Engineering Electronics II" conducted through online learning at Walla Walla University. We ([Jordyn Watkins](https://github.com/greenjacketgirl) and [Joshua Silver](https://github.com/JoshSilver8)) were tasked with designing, building, and testing a *software defined radio (SDR) receiver*. Our radio is designed to listen to frequencies ranging from 500kHz - 50MHz. For more information on the theory, reasoning behind our design choices, and a more in depth look at the results and specs of this project, please refer to the [Wiki](https://github.com/greenjacketgirl/SDR_Receiver/wiki) tab.

**Navigation** | This repository consists of several folders. In this "code" tab, you will find 2 primary folders: Attenuator and Receiver. Within the attenuator file, you will find a folder containing the KiCad files, a folder containing the LTspice simulation files, and a third folder containing build and test notes with pictures and other documentation. The Receiver folder contains 4 main folders: KiCad, LTSpice, Quisk, and Documentation. Note that  

**Results** | The radio is in working condition - producing low noise I and Q signals 90 degrees out of phase. The signal discernability is very good, being able to detect signals as small as 0.5uV, and the image rejection is also decent having a 30dB difference between signal and image. For more details on the specs for the radio, visit the [Results](https://github.com/greenjacketgirl/SDR_Receiver/wiki/Results) in the [Wiki](https://github.com/greenjacketgirl/SDR_Receiver/wiki).

**Credits** | This project was created with a lot of help from our professor, Dr. Frohne. The files under the Quisk folder are primarily his. See his github profile at https://github.com/frohro/ 

**Status of Project** | Visit the "issues" tab to see errors and fixes for this project - which should provide a more in depth explanation for the quote "status" of the project. You can also visit the "Wiki" page or view the documentation files in the folders for a description of build and test process when troubleshooting issues.

REVISION 1: _05/26/2020  Build Phase and Troubleshooting Hardware_ |
REVISION 2: _06/04/2020 Test Phase and Troubleshooting Quisk Software Integration_ | REVISION 3: _06/10/2020 Working Radio Fine Tuning and Adjustments_
