import serial, time, statistics, csv


REF_VAL = 0
SET_VAL = 0
VERN_VAL = 0
REF_LIST = []
SetPoint = [-30, -20, 0, 30, 40]            # temperature set points. If the amount of set points changes edit line 397
p = 0                                       # temperature set point list index variable
BathError = 0
DUT10 = 0
DUT11 = 0
DUT12 = 0
DUT13 = 0
DUT14 = 0
DUT15 = 0
DUT16 = 0
DUT17 = 0
DUT18 = 0
DUT19 = 0


print('**************************************************************************')
print('           Electrical Resistance Thermometer Calibration ')
print('**************************************************************************\n\n\n')


print('Please enter the COM port that the Fluke temperature bath is connected to:')
bath_port = (input('>'))
bath_port = bath_port.upper()

ser_bath = serial.Serial(bath_port, 2400, timeout=5)          #Serial port initialsation

bath_open = ser_bath.is_open   # Test to see if connection successful
if bath_open == True:
    print('Connection to temperature bath successful. ')
else:
    print('Connection unsuccessful. Please reset the port and restart the program. ')
    time.sleep(10)
    exit()                   # If connection not successful end program. This could be improved by asking the user to re-enter port details


print('**************************************************************************\n\n')

print('Please enter the COM port that the ISOTECH microK is connected to:')
microK_port = (input('>'))
microK_port = microK_port.upper()


ser_plex = serial.Serial(microK_port, 9600, timeout=5)

mux_open = ser_plex.is_open
print(mux_open)
if mux_open == True:
    print('Connection to microK successful. ')
else:
    print('Connection unsuccessful. Please reset the port and restart the program. ')
    time.sleep(10)
    exit()

print('**************************************************************************\n\n')


def BathSetPoint(ser_bath):         # Get the current set point of the bath
    try:
        global SET_VAL
        ser_bath.write(b's\r\n')
        time.sleep(2)
        line = ser_bath.readline()  # Read instrument serial output
        line_str = str(line)  # Convert data to string

        form_str = line_str[7:-6]
        SET_VAL = float(form_str)

        return SET_VAL
    except ValueError:
        print('NaN')

def VernVal(ser_bath):          # Get current vernier adjustment value.
    try:
        global VERN_VAL
        ser_bath.write(b'v\r\n')
        time.sleep(2)
        line = ser_bath.readline()  # Read instrument serial output
        line_str = str(line)  # Convert data to striNG

        form_str = line_str[4:-5]
        VERN_VAL = float(form_str)

        return VERN_VAL
    except ValueError:
        print('Nan')

def SetVern(ser_bath, error, VernVal):          # Set vernier adjustment value
    try:
        corr = VernVal + error
        ser_bath.write(b'v=%a\r\n'%corr)
        time.sleep(2)
        print('correction: ',corr)

    except:
        print('Vernier set error')



def read_REF(ser_plex):                 # Read the current temperature of the reference thermometer
    try:
        global REF_VAL
        ser_plex.write(b'READ2?\r\n')
        time.sleep(5)
        linePlex = ser_plex.readline()
        # Read instrument serial output
        # Convert data to string
        plexline_str = str(linePlex)

        form_str = plexline_str[2:-6]
        REF_VAL = float(form_str)

        return REF_VAL

    except ValueError:
        return print('ValueError')






def read_DUT10(ser_plex):                   # Read the resistance value of channel 10 DUT
    global DUT10
    ser_plex.write(b'MEAS:FRES10:REF204? 125,1\r\n')
    time.sleep(2)
    linePlex = ser_plex.readline()
    plexline_str = str(linePlex)

    form_str = plexline_str[2:-3]
    DUT10 = float(form_str)


    return DUT10


def read_DUT11(ser_plex):
    global DUT11
    ser_plex.write(b'MEAS:FRES11:REF204? 125,1\r\n')
    time.sleep(2)
    linePlex = ser_plex.readline()
    plexline_str = str(linePlex)

    form_str = plexline_str[2:-3]
    DUT11 = float(form_str)


    return DUT11


def read_DUT12(ser_plex):
    global DUT12
    ser_plex.write(b'MEAS:FRES12:REF204? 125,1\r\n')
    time.sleep(2)
    linePlex = ser_plex.readline()
    plexline_str = str(linePlex)

    form_str = plexline_str[2:-3]
    DUT12 = float(form_str)

    return DUT12


def read_DUT13(ser_plex):
    global DUT13
    ser_plex.write(b'MEAS:FRES13:REF204? 125,1\r\n')
    time.sleep(2)
    linePlex = ser_plex.readline()
    plexline_str = str(linePlex)

    form_str = plexline_str[2:-3]
    DUT13 = float(form_str)

    return DUT13


def read_DUT14(ser_plex):
    global DUT14
    ser_plex.write(b'MEAS:FRES14:REF204? 125,1\r\n')
    time.sleep(2)
    linePlex = ser_plex.readline()
    plexline_str = str(linePlex)

    form_str = plexline_str[2:-3]
    DUT14 = float(form_str)

    return DUT14


def read_DUT15(ser_plex):
    global DUT15
    ser_plex.write(b'MEAS:FRES15:REF204? 125,1\r\n')
    time.sleep(2)
    linePlex = ser_plex.readline()
    plexline_str = str(linePlex)

    form_str = plexline_str[2:-3]
    DUT15 = float(form_str)

    return DUT15


def read_DUT16(ser_plex):
    global DUT16
    ser_plex.write(b'MEAS:FRES16:REF204? 125,1\r\n')
    time.sleep(2)
    linePlex = ser_plex.readline()
    plexline_str = str(linePlex)

    form_str = plexline_str[2:-3]
    DUT16 = float(form_str)

    return DUT16


def read_DUT17(ser_plex):
    global DUT17
    ser_plex.write(b'MEAS:FRES17:REF204? 125,1\r\n')
    time.sleep(2)
    linePlex = ser_plex.readline()
    plexline_str = str(linePlex)

    form_str = plexline_str[2:-3]
    DUT17 = float(form_str)

    return DUT17


def read_DUT18(ser_plex):
    global DUT18
    ser_plex.write(b'MEAS:FRES18:REF204? 125,1\r\n')
    time.sleep(2)
    linePlex = ser_plex.readline()
    plexline_str = str(linePlex)

    form_str = plexline_str[2:-3]
    DUT18 = float(form_str)

    return DUT18


def read_DUT19(ser_plex):
    global DUT19
    ser_plex.write(b'MEAS:FRES19:REF204? 125,1\r\n')
    time.sleep(2)
    linePlex = ser_plex.readline()
    plexline_str = str(linePlex)

    form_str = plexline_str[2:-3]
    DUT19 = float(form_str)

    return DUT19


start = time.time()          # Start program timer. measures program run time and print result when test has completed

#Set initial bath conditions
print('Setting initial bath conditions...')
ser_bath.write(b'du=h\r\n')     #Turn off continuous output and duplex to half duplex
time.sleep(2)
ser_bath.write(b'sa=0\r\n')
time.sleep(2)
ser_bath.write(b'v=0\r\n')      # Set the initial vernier setting to 0.0
time.sleep(5)
ser_bath.reset_input_buffer()
time.sleep(2)

ser_bath.write(b's=%a\r\n'%(SetPoint[p]+BathError))     #Set beth temp to first set point
time.sleep(2)
ser_bath.reset_input_buffer()
print('Initial bath conditions set. ')
print('Set point: ', SetPoint[p])


while True:
    try:

        read_REF(ser_plex)      # Read the current value of the reference SPRT

        REF_LIST.insert(0, REF_VAL)     # Add that value to index [0] of the temperature list


        if len(REF_LIST) >= 10:
            vari = statistics.stdev(REF_LIST[:9])       # Calculate the stdev of the past 10 temperature readings
            mean = statistics.mean(REF_LIST[:9])        # Calculate the mean temperature of the past 10 temperature readings
            print('Waiting for bath stability')
            print("stdev: ", vari)
            if vari < 0.00018:                      # Once the stdev is below 0.00018 the temperature of the bath is stable
                print("Bath is stable!")
                print("Mean temperature: ", mean)

                error = SetPoint[p] - mean          # Calculate the error between the set point value and actual value

                print("ERROR: ", error)

                if error >= 0.001:

                    if error >= 0.01:                   # If error larger than 0.01 adjust the set point value
                        print('Making Corrections...')
                        BathError = BathError + error
                        ser_bath.write(b's=%a\r\n'%(SetPoint[p]+BathError))
                        time.sleep(60)                  # Wait 60 sec before taking another temp reading to allow the temperature to change
                        ser_bath.reset_input_buffer()
                        print('Corrections made.')

                    else:
                        print('Making vernier corrections...')     # If the error is only small use the vernier adjustment
                        VernVal(ser_bath)
                        print('current vernier setting: ', VERN_VAL)

                        SetVern(ser_bath, error, VERN_VAL)
                        time.sleep(60)
                        print('Corrections made.')


                elif error <= -0.001:               # Same as above for negative error

                    if error <= -0.01:
                        print('Making corrections...')
                        BathError = BathError + error
                        ser_bath.write(b's=%a\r\n'%(SetPoint[p]+BathError))
                        time.sleep(60)
                        ser_bath.reset_input_buffer()
                        print('Corrections made.')

                    else:
                        print('Making vernier corrections')
                        VernVal(ser_bath)
                        print('current vernier setting: ', VERN_VAL)

                        SetVern(ser_bath, error, VERN_VAL)
                        time.sleep(60)                          # Do not reduce the wait period
                        print('Corrections made.')

                else:
                    print("Correct temp achieved. Taking DUT readings") # If the error is less than =/-0.001 the correct temp has been achieved

                    BathSetPoint(ser_bath)      # Read bath

                    read_DUT10(ser_plex)        # Read DUT values
                    read_DUT11(ser_plex)
                    read_DUT12(ser_plex)
                    read_DUT13(ser_plex)
                    read_DUT14(ser_plex)
                    read_DUT15(ser_plex)
                    read_DUT16(ser_plex)
                    read_DUT17(ser_plex)
                    read_DUT18(ser_plex)
                    read_DUT19(ser_plex)
                    print('Set Point: ', SET_VAL)       # Print values to terminal for operator reference
                    print('Channel 10: ', DUT10)
                    print('Channel 11: ', DUT11)
                    print('Channel 12: ', DUT12)
                    print('Channel 13: ', DUT13)
                    print('Channel 14: ', DUT14)
                    print('Channel 15: ', DUT15)
                    print('Channel 16: ', DUT16)
                    print('Channel 17: ', DUT17)
                    print('Channel 18: ', DUT18)
                    print('Channel 19: ', DUT19)

                    with open('ERT_testdata.csv', 'a', newline='') as csvfile:
                        fieldnames = ['DUT Resistance', 'Reference Temperature', 'Current set point',   # Append .CSV file with recoreded data
                                      '']                # logged varibles: DUT resistance, Reference temp, set point
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow({'DUT Resistance': DUT10, 'Reference Temperature': REF_VAL,
                                         'Current set point': SetPoint[p]})
                        writer.writerow({'DUT Resistance': DUT11, 'Reference Temperature': REF_VAL,
                                         'Current set point': SetPoint[p]})
                        writer.writerow({'DUT Resistance': DUT12, 'Reference Temperature': REF_VAL,
                                         'Current set point': SetPoint[p]})
                        writer.writerow({'DUT Resistance': DUT13, 'Reference Temperature': REF_VAL,
                                         'Current set point': SetPoint[p]})
                        writer.writerow({'DUT Resistance': DUT14, 'Reference Temperature': REF_VAL,
                                         'Current set point': SetPoint[p]})
                        writer.writerow({'DUT Resistance': DUT15, 'Reference Temperature': REF_VAL,
                                         'Current set point': SetPoint[p]})
                        writer.writerow({'DUT Resistance': DUT16, 'Reference Temperature': REF_VAL,
                                         'Current set point': SetPoint[p]})
                        writer.writerow({'DUT Resistance': DUT17, 'Reference Temperature': REF_VAL,
                                         'Current set point': SetPoint[p]})
                        writer.writerow({'DUT Resistance': DUT18, 'Reference Temperature': REF_VAL,
                                         'Current set point': SetPoint[p]})
                        writer.writerow({'DUT Resistance': DUT19, 'Reference Temperature': REF_VAL,
                                         'Current set point': SetPoint[p]})
                    time.sleep(1)

                    p += 1          # Increment the set point to the next value

                    if p >= 5:      # Once all set points have been tested the program will have completed.
                        print('Test complete. Generated .CSV file can be found at:  ') # .CSV file path
                        end = time.time()
                        print('Test runtime: ', (end - start))  # print program run time
                        time.sleep(30)
                        exit()      # End program
                    else:
                        print('Set point: ', SetPoint[p])


                    ser_bath.write(b's=%a\r\n' % (SetPoint[p] + BathError))    # Set the bath to the next set point
                    time.sleep(60)
                    ser_bath.reset_input_buffer()
                    ser_bath.write(b'v=0\r\n')      # Reset the vernier adjustment to 0.0 to prevent limit errors
                    time.sleep(5)
                    ser_bath.reset_input_buffer()

            else:
                print("Temperature not stable!")        # If bath temp not stable
        else:
            continue





    except AttributeError:
        print('NaN')
