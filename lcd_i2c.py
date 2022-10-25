import smbus
from time import sleep

class lcd_i2c:

    bus = smbus.SMBus(1)
    ADDRESS = None
    WIDTH = None
    LINES = None
    BACKLIGHT = None

    LCD_CHR = 1 # Mode - Sending data
    LCD_CMD = 0 # Mode - Sending command

    # Memory addresses for the lines
    LCD_LINE_1_ADDRESS = 0x80
    LCD_LINE_2_ADDRESS = 0xC0
    LCD_LINE_3_ADDRESS = 0x94
    LCD_LINE_4_ADDRESS = 0xD4

    BACKLIGHT_ON = 0x08
    BACKLIGHT_OFF = 0x00

    ENABLE = 0b00000100 # Enable bit

    # Timing constants
    E_PULSE = 0.0005
    E_DELAY = 0.0005

    def __init__(self, address = 0x27, width = 16, lines = 2, backlight = True):
        self.ADDRESS = address
        self.WIDTH = width
        self.LINES = lines
        if backlight:
            self.BACKLIGHT = self.BACKLIGHT_ON
        else:
            self.BACKLIGHT = self.BACKLIGHT_OFF

        # Initialise display
        self.lcd_write_byte(0x33, self.LCD_CMD) # 110011 Initialise
        self.lcd_write_byte(0x32, self.LCD_CMD) # 110010 Initialise
        self.lcd_write_byte(0x06, self.LCD_CMD) # 000110 Cursor move direction
        self.lcd_write_byte(0x0C, self.LCD_CMD) # 001100 Display On, Cursor Off, Blink Off
        self.lcd_write_byte(0x28, self.LCD_CMD) # 101000 Data length, number of lines, font size
        self.lcd_write_byte(0x01, self.LCD_CMD) # 000001 Clear display
        sleep(self.E_DELAY)

    def lcd_toggle_enable(self, byte):
        """Enables toggle."""
        sleep(self.E_DELAY)
        self.bus.write_byte(self.ADDRESS, (byte | self.ENABLE))
        sleep(self.E_PULSE)
        self.bus.write_byte(self.ADDRESS,(byte & ~self.ENABLE))
        sleep(self.E_DELAY)

    def lcd_write_byte(self, byte, mode):
        """Send one byte of data to the i2c backpack.
        byte: the data to send
        mode: sending data or a command. 1 for data, 0 for a command.
        """

        byte_high = mode | (byte & 0xF0) | self.BACKLIGHT
        byte_low = mode | (byte << 4) & 0xF0 | self.BACKLIGHT

        self.bus.write_byte(self.ADDRESS, byte_high)
        self.lcd_toggle_enable(byte_high)

        self.bus.write_byte(self.ADDRESS, byte_low)
        self.lcd_toggle_enable(byte_low)

    def println(self, string, line):
        """Writes a string to the LCD on the specified line.
        This method will ignore all extra characters that don't fit on the
        specified line.
        string: the string to be printed
        line: the line on which it will be printed
        """

        string = string.ljust(self.WIDTH, " ")

        # Tell where in the memory the string has to be written to
        line_address = self.LCD_LINE_1_ADDRESS
        if line == 1:
            line_address = self.LCD_LINE_1_ADDRESS
        elif line == 2:
            line_address = self.LCD_LINE_2_ADDRESS
        elif line == 3:
            line_address = self.LCD_LINE_3_ADDRESS
        elif line == 4:
            line_address = self.LCD_LINE_4_ADDRESS
        self.lcd_write_byte(line_address, self.LCD_CMD)

        for i in range(self.WIDTH): # Extra characters will be ignored.
            self.lcd_write_byte(ord(string[i]), self.LCD_CHR)

    def print_str(self, string, scroll_time = 5):
        """Writes a string to the LCD.
        This method will display all text given in the string variable. If the
        string contains more characters than can be displayed, it will scrol
        through the text.
        string: the string to be printed
        scroll_time: the time in seconds to wait before printing the next line
        """

        if len(string) <= self.WIDTH:
            self.println(string, 1)

        # Split string into chunks of a WIDTH number of characters
        lines = [string[i:i+self.WIDTH] for i in range(0, len(string), self.WIDTH)]

        i = len(lines)
        j = 0
        if i <= self.LINES: # No need to scroll
            while j < i:
                self.println(lines[j], j + 1)
                j = j + 1
        else: # Need to scroll through the string
            while j < i:
                if j + 1 == i:
                    break
                k = 0
                while k < (self.LINES + 1):
                    try:
                        self.println(lines[j + k], k + 1)
                    except IndexError: # We're done printing everything.
                        pass
                    k = k + 1
                sleep(scroll_time)
                j = j + 1

    def clear(self):
        """Clears all the text on the LCD."""

        for i in range(self.LINES):
            self.print_str(" ", i)

    def receiveMessage(self):
        """Receive the message sended by the other board"""
        server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
  
        port = 2
        server_sock.bind(("",port))
        server_sock.listen(1)
      
        client_sock,address = server_sock.accept()
        print("Accepted connection from " + str(address))
      
        data = client_sock.recv(1024)
        print("received [%s]" % data)
        sleep(1)
        client_sock.close()
        server_sock.close()
        return data


if __name__ == "__main__":
    lcd = lcd_i2c()
    for i in range(10, 0, -1):
        lcd.print_str("Calculating..." + str(i), 1)

    data = lcd.receiveMessage()
    lcd.print_str("Your bpm is: " + data, 1)

