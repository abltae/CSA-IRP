import serial
import struct
import mysql.connector
from ence import *

mydb = mysql.connector.connect(host="localhost",username = "root",password = "", database = "uidbytes")
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE cards(id INT AUTO_INCREMENT PRIMARY KEY, uid VARCHAR(255), name VARCHAR(255))") //ONLY RUN THIS ONCE TO MAKE A TABLE
serialPort = serial.Serial(
    port="COM3", baudrate=9600
)
serialString = ""
array = []
int = 0;
name = input("Card Holder Name: ")
while 1:

    serialPort.reset_output_buffer()
    if serialPort.in_waiting >= 4:

        serialString = serialPort.read(4)
        unpacked_data = struct.unpack('BBBB', serialString)

        int_value1 = unpacked_data[0]
        int_value2 = unpacked_data[1]
        int_value3 = unpacked_data[2]
        int_value4 = unpacked_data[3]

        # Print the unpacked integer values
        # print("\n", int_value1, int_value2, int_value3, int_value4)
        array.append((int_value1.to_bytes(2,'big')))
        array.append((int_value2.to_bytes(2,'big')))
        array.append((int_value3.to_bytes(2,'big')))
        array.append((int_value4.to_bytes(2,'big')))
        int += 1
        if int == 3:
            break;

result = ""


for byte in array:
    result += str(byte)

print("Before Encryption: " + result)
a = encryptDecrypt(result,'APCSA')
print("After Encryption: "+ a)

sql = "INSERT INTO cards (uid, name) VALUES (%s , %s)"

val = (a, name)
mycursor.execute(sql,val)

mydb.commit()

