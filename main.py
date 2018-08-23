import serial
import time
import statistics
import csv
import matplotlib as plt
from numpy import array


SET_VAL = 0
VERN_VAL = 0
REF_LIST = []
SetPoint = [-30, -20, 0, 30, 40]
p = 0
BathError = 0
REF_VAL = 0
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

ser_bath = serial.Serial(bath_port, 2400, timeout=5)

bath_open = ser_bath.is_open
if bath_open:
    print('Connection to temperature bath successful. ')
else:
    print('Connection unsuccessful. Please reset the port and restart the program. ')
    time.sleep(10)
    exit()


print('**************************************************************************\n\n')

print('Please enter the COM port that the ISOTECH microK is connected to:')
microK_port = (input('>'))
microK_port = microK_port.upper()


ser_plex = serial.Serial(microK_port, 9600, timeout=5)

mux_open = ser_plex.is_open
if mux_open:
    print('Connection to microK successful. ')
else:
    print('Connection unsuccessful. Please reset the port and restart the program. ')
    time.sleep(10)
    exit()

print('**************************************************************************\n\n')


def BathSetPoint(ser_bath):
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

def VernVal(ser_bath):
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

def SetVern(ser_bath, error, VernVal):
    try:
        corr = VernVal + error
        ser_bath.write(b'v=%a\r\n'%corr)
        time.sleep(2)
        print('correction: ',corr)

    except ValueError:
        print('Vernier set error')



def read_REF(ser_plex):
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



def read_DUT10(ser_plex):
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


start = time.time()

#Set initial bath conditions
print('Setting initial bath conditions...\n')
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
print('Waiting for bath temperature stability\n')

while True:
    try:

        read_REF(ser_plex)

        REF_LIST.insert(0, REF_VAL)


        if len(REF_LIST) >= 10:
            vari = statistics.stdev(REF_LIST[:9])
            mean = statistics.mean(REF_LIST[:9])

            if vari < 0.00018:
                print("Bath is stable!")
                print("Mean temperature: ", mean)

                error = SetPoint[p] - mean

                print("ERROR: ", error)


                if error >= 0.001:

                    if error >= 0.01:
                        print('Making Corrections...')
                        BathError = BathError + error
                        ser_bath.write(b's=%a\r\n'%(SetPoint[p]+BathError))
                        time.sleep(60)
                        ser_bath.reset_input_buffer()
                        print('Corrections made.')
                        print('Waiting for stabilisation\n')

                    else:
                        print('Making vernier corrections...')
                        VernVal(ser_bath)
                        print('current vernier setting: ', VERN_VAL)

                        SetVern(ser_bath, error, VERN_VAL)
                        time.sleep(60)
                        print('Corrections made.')
                        print('Waiting for stabilisation\n')


                elif error <= -0.001:

                    if error <= -0.01:
                        print('Making corrections...')
                        BathError = BathError + error
                        ser_bath.write(b's=%a\r\n'%(SetPoint[p]+BathError))
                        time.sleep(60)
                        ser_bath.reset_input_buffer()
                        print('Corrections made.')
                        print('Waiting for stabilisation\n')

                    else:
                        print('Making vernier corrections')
                        VernVal(ser_bath)
                        print('current vernier setting: ', VERN_VAL)

                        SetVern(ser_bath, error, VERN_VAL)
                        time.sleep(60)
                        print('Corrections made.')
                        print('Waiting for stabilisation\n')

                else:
                    print("Correct temp achieved. Taking DUT readings\n")

                    BathSetPoint(ser_bath)

                    read_DUT10(ser_plex)
                    read_DUT11(ser_plex)
                    read_DUT12(ser_plex)
                    read_DUT13(ser_plex)
                    read_DUT14(ser_plex)
                    read_DUT15(ser_plex)
                    read_DUT16(ser_plex)
                    read_DUT17(ser_plex)
                    read_DUT18(ser_plex)
                    read_DUT19(ser_plex)
                    print('Set Point: ', SET_VAL)
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
                        fieldnames = ['Channel','DUT Resistance', 'Reference Temperature', 'Set point',
                                      '']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow({'Channel':'Channel 10', 'DUT Resistance': DUT10, 'Reference Temperature': REF_VAL,
                                         'Set point': SetPoint[p]})
                        writer.writerow({'Channel':'Channel 11', 'DUT Resistance': DUT11, 'Reference Temperature': REF_VAL,
                                         'Set point': SetPoint[p]})
                        writer.writerow({'Channel':'Channel 12', 'DUT Resistance': DUT12, 'Reference Temperature': REF_VAL,
                                         'Set point': SetPoint[p]})
                        writer.writerow({'Channel':'Channel 13', 'DUT Resistance': DUT13, 'Reference Temperature': REF_VAL,
                                         'Set point': SetPoint[p]})
                        writer.writerow({'Channel':'Channel 14', 'DUT Resistance': DUT14, 'Reference Temperature': REF_VAL,
                                         'Set point': SetPoint[p]})
                        writer.writerow({'Channel':'Channel 15', 'DUT Resistance': DUT15, 'Reference Temperature': REF_VAL,
                                         'Set point': SetPoint[p]})
                        writer.writerow({'Channel':'Channel 16', 'DUT Resistance': DUT16, 'Reference Temperature': REF_VAL,
                                         'Set point': SetPoint[p]})
                        writer.writerow({'Channel':'Channel 17', 'DUT Resistance': DUT17, 'Reference Temperature': REF_VAL,
                                         'Set point': SetPoint[p]})
                        writer.writerow({'Channel':'Channel 18', 'DUT Resistance': DUT18, 'Reference Temperature': REF_VAL,
                                         'Set point': SetPoint[p]})
                        writer.writerow({'Channel':'Channel 19', 'DUT Resistance': DUT19, 'Reference Temperature': REF_VAL,
                                         'Set point': SetPoint[p]})
                    time.sleep(1)

                    p += 1

                    if p >= 5:
                        print('Test complete. Generated .CSV file can be found at:  ')
                        end = time.time()
                        print('Test runtime: ', (end - start))


                        y = array(REF_LIST)
                        plt.plot(y)
                        plt.ylabel('Temperature')
                        plt.show()

                        ser_bath.reset_input_buffer()
                        time.sleep(30)

                        ser_bath.write(b's=20\r\n')
                        time.sleep(30)
                        ex = input('To exit the program press any key')
                        exit()


                    else:
                        print('Set point: ', SetPoint[p])


                    ser_bath.write(b's=%a\r\n' % (SetPoint[p] + BathError))
                    time.sleep(60)
                    ser_bath.reset_input_buffer()
                    ser_bath.write(b'v=0\r\n')
                    time.sleep(5)
                    ser_bath.reset_input_buffer()

            else:
                continue
        else:
            continue





    except AttributeError:
        print('NaN')