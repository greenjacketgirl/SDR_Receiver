# Navigating this folder

This folder contains two versions of the schematic and pcb design. The first design is the collection of files shown. The second revision is located in the folder [Kicad-V2](https://github.com/greenjacketgirl/SDR_Receiver/tree/master/SDR%20Receiver/KiCad/Kicad-V2). This second revision is the schematic updated with the corrections made by hand shown in the [Issues tab](https://github.com/greenjacketgirl/SDR_Receiver/issues). Note that this second revision only has an updated schematic, not an updated pcb. Thus, future work will require further revision of the PCB. 

Primary corrections made in this second revision:
* crystal footprint pin numbers corrected
* pull up resistors on si5351 clock generator connected to VCC instead of GND
* bandpass filter wiring correction on multiplexer
* label correction from tayloe mixer to summing op-amps

I tried to include the .pretty and library files for the footprints and schematic symbols I used. If you have a difficult time seeing the footprints for some reason, you can also refer to our digikey BOM in the [documents section](https://github.com/greenjacketgirl/SDR_Receiver/tree/master/SDR%20Receiver/Documentation) to look up the part on the [digikey website](https://www.digikey.com) and download the respective footprint from there. You may need to also make corrections to the PCB board after uploading a new symbol and footprint .pretty file.
