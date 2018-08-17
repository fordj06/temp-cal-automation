# temp-cal-automation
Python script to automate the process of ERT temperature sensor calibration using the Fluke 7341 temperature bath and a ISOTECH microK precision resistance bridge with a ISOTECH microsKanner multiplexer.


### REV 0.1: 
This initial commit meets the basic requirements but can be greatly improved in terms of both features and code cleanliness. 

Current function:
- Set initial bath conditions 
- Poll reference temperature 
- Calculate bath temperature stability by calculating the stdev of the previous 10 reference temp results
- Once the bath is determined to be stable, calculate error
- Make bath adjustments to correct for any error
- Once stability and the correct temperature have been achieved take DUT (device under test) resistance readings
- Write results to a .CSV file 
- Change bath temperature to the next pre-defined set point
- Set bath vernier adjustment to 0 


NOTE: The bath front panel interface is directly linked to the serial output and can cause communication issues if not left on the current temperature reading. Other parameters can be checked during testing but it is essential that you return to the current temperature reading screen before the temperature stabilises. 

Possible improvements: 
- User interface
- Improved error checking
- Automatically store results on ServiceNow database 
- Auto generate calibration certificates 
