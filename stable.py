import serial, re, time, statistics

REF_LIST = []
SetPoint = [-30, -20, 0, 30, 40]

ser_plex = serial.Serial('COM9', 9600, timeout=5)

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

def read_REF(ser_plex):
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

if ser_plex.isOpen():
    print(ser_plex.name + ' is open...')
else:
    print("Bridge/MUX Instrument Not Connected")

while True:
    try:
        read_REF(ser_plex)

        REF_LIST.insert(0, REF_VAL)

        localtime = time.asctime(time.localtime(time.time()))

        print("Reference Temp: ", REF_VAL)
        print("time: ", localtime)
        print(REF_LIST)
        print(len(REF_LIST))

        if len(REF_LIST) >= 10:
            vari = statistics.stdev(REF_LIST[:9])
            mean = statistics.mean(REF_LIST[:9])
            print("stdev: ", vari)
            if vari < 0.00018:
                print("Bath is stable!")
                print("Mean temperature: ", mean)

                error = mean - SetPoint[4]

                print("ERROR: ", error)

                if error >= 0.001:

                    print("make vernier adjustment")

                elif error <= -0.001:

                    print("Make vernier adjustment")

                else:
                    print("Correct temp achieved. Take DUT readings")

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

                    time.sleep(1)

            else:
                print("Temperature not stable!")
        else:
            continue





    except AttributeError:
        print('NaN')
