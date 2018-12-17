# Kenny De Klerck
#2018.12.17

# import libraries
import serial
import threading

# serial Ports
serialPortOut = serial.Serial(port = "COM4", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serialPortIn1 = serial.Serial(port = "COM5", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serialPortIn2 = serial.Serial(port = "COM6", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

# text files
textOut1 = "output1.txt"
textOut2 = "output2.txt"

# serial reading thread
def worker (serialPort, exportFile):
    # read from serial port
    line = serialPort.readline()

    # write to file file
    f = open (exportFile, "a")
    f.write (line)

# main loop
if __name__ == "main":
    # update console
    print ("Start serial test program")

    # create serial input threads
    threadIn1 = threading.Thread (target = worker, args = (serialPortIn1, textOut1))
    threadIn2 = threading.Thread (target = worker, args = (serialPortIn2, textOut2))

    # start threads
    threadIn1.start()
    threadIn2.start()

    # Open serial output port
    serialPortOut.open()

    # Send to serial out
    for loop in range (100):
        # Send to serial
        serial.write(loop)

    # Close serial out
    serialPortOut.close()

    # force threads to close
    threadIn1.join()
    threadIn2.join()

