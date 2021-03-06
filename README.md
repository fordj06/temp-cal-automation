# ERT Automated Calibration 
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

### Manual instrument setup 

The Instrument setup is much the same as for the manual test. The steps are: 

   1. Ensure the instruments are connected. 
   2. Turn on the instruments 
   3. Set the bath to -30 to begin cooling (not essential but speeds up the testing process).
   4. Connect the ERTs to the microsKanner terminals 
   5. Put the ERTs into the bath 
   6. Once all the ERTs are connected turn the channels on to test the connections
   7. Place the SPRT working reference standard into the bath 
   8. Start the application on the workstation 
   9. Follow instructions oth the application terminal 

### microK & microsKanner notes:

The SPRT setting are adjusted via the front panel of the instrument however the DUT settings are controlled via the script. They are currently hardcoded as ``` MEAS:FRES10:REF204? 125,1 ```. This equates to, measure resistance of channel 10 uding channel 3 of the microK (REF204) with a range of 125 ohms and a current of 1mA. These values could be incorporated into the GUI. 



### Making a .py File Into a Stand Alone Executable

https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263 

