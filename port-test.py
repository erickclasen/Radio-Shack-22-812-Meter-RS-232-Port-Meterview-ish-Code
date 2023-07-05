'''
06-25-2023 Erick Clasen

Questions or Comments...
Facebook: https://www.facebook.com/erickclasen
Twitter: https://twitter.com/clasen_erick
Github: https://github.com/erickclasen


Scan all the serial ports and report open ports.
Makes it easy to see what is up and running.

Code created using ChatGPT

See the following page for more ways to deal with serial ports...
https://www.cyberciti.biz/hardware/5-linux-unix-commands-for-connecting-to-the-serial-console/

Helpful commands while (re)learning serial ports in 2023.

List ports that are recoginized on startup...
dmesg | egrep -i --color 'serial|ttyS'

Example of communicting with a port. In this case this was for the
Radio Shack 22-812 digital multimeter. It will display gibberish characters
when hooked up. This was a sanity check to see some output from the meter
before trying to connect to it with meter software.

cu -l /dev/ttyS0 -s 4800


Requirements

serial

pip install pyserial

https://pyserial.readthedocs.io/en/latest/pyserial.html


'''
import serial.tools.list_ports

# Get a list of available serial ports
ports = serial.tools.list_ports.comports()

# Print the list of ports
for port in ports:
    print(f"Found port: {port.device}")

# Iterate over the ports and try to open them
for port in ports:
    try:
        # Open the port
        ser = serial.Serial(port.device, 4800) #9600)  # Adjust the baud rate if needed

        # Read a line of data from the port
        data = ser.readline().decode().strip()
        if data:
            print(f"Data received on {port.device}: {data}")

        # Close the port
        ser.close()
    except serial.SerialException:
        pass  # Ignore any errors when trying to open the port

