using FTD2XX_NET;
using System;

namespace project
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declare variables
            FTDI.FT_STATUS ftStatus = FTDI.FT_STATUS.FT_OK;
            uint dwNumDevs = 0;
            uint uiDevIndex = 0xF;
            byte[] outputBuffer = new byte[1024];
            byte[] inputBuffer = new byte[1024];
            uint dwCount = 0;
            uint dwNumBytesToSend = 0;
            uint dwNumBytesSent = 0;
            uint dwNumBytesToRead = 0;
            uint dwNumBytesRead = 0;
            uint dwClockDivisor = 0x05DB;
            FTDI ftHandle = new FTDI();

            // Check for FTDI devices
            Console.WriteLine("Checking for FTDI devices...\n");
            ftStatus = FTDI.FT_CreateDeviceInfoList(ref dwNumDevs);
            if (ftStatus != FTDI.FT_STATUS.FT_OK)
            {
                Console.WriteLine("Error in getting the number of devices\n ");
                Console.ReadLine();
                return;
            }
            if (dwNumDevs < 1)
            {
                Console.WriteLine("There are no FTDI devices installed\n");
                Console.ReadLine();
                return;
            }
            Console.WriteLine($"{dwNumDevs} FTDI devices found-the count includes individual ports on a single chip \n");
            Console.WriteLine("\nAssume first device has the MPSSE and open it...\n");

            // Open first device
            ftStatus = ftHandle.OpenByIndex(uiDevIndex);
            if (ftStatus != FTDI.FT_STATUS.FT_OK)
            {
                Console.WriteLine($"Open failed with error {ftStatus}\n");
                Console.ReadLine();
                return;
            }
            Console.WriteLine("\nConfiguring port for MPSSE use...\n");
            ftStatus |= ftHandle.ResetDevice();
            ftStatus |= ftHandle.GetQueueStatus(ref dwNumBytesToRead);
            if (ftStatus == FTDI.FT_STATUS.FT_OK && dwNumBytesToRead > 0)
            {
                ftStatus |= ftHandle.Read(inputBuffer, dwNumBytesToRead, ref dwNumBytesRead);
                ftStatus |= ftHandle.SetUSBParameters(65536, 65535);
                ftStatus |= ftHandle.SetChars(false, 0, false, 0);
                ftStatus |= ftHandle.SetTimeouts(0, 5000);
                ftStatus |= ftHandle.SetLatency(16);
                ftStatus |= ftHandle.SetBitMode(0x0, 0x00);
                ftStatus |= ftHandle.SetBitMode(0x0, 0x02);
            }
            if (ftStatus != FTDI.FT_STATUS.FT_OK)
            {
                Console.WriteLine($"Error in initializing the MPSSE
                                   // Check
for MPSSE command response
Thread.Sleep(50);
outputBuffer[dwNumBytesToSend++] = 0xAA;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref dwNumBytesSent);
dwNumBytesToSend = 0;
do
{
ftStatus = ftHandle.GetQueueStatus(ref dwNumBytesToRead);
// Get the number of bytes in the device input buffer
}
while (dwNumBytesToRead == 0 & & ftStatus == FTDI.FT_STATUS.FT_OK);
// or Timeout
bool
bCommandEchod = false;
ftStatus = ftHandle.Read(inputBuffer, dwNumBytesToRead, ref
dwNumBytesRead);
// Read
out
the
data
from input buffer

for (dwCount = 0; dwCount < dwNumBytesRead - 1; dwCount++)
    // Check if Bad
    command and echo
    command
    received
{
if (inputBuffer[dwCount] == 0xFA & & inputBuffer[dwCount + 1] == 0xAA)
{
    bCommandEchod = true;
break;
}
}
if (!bCommandEchod)
{
Console.WriteLine("MPSSE not responding\n");
ftHandle.Close();
return 1;
}

// Set
clock
frequency
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x8A;
outputBuffer[dwNumBytesToSend + +] = (byte)(dwClockDivisor & 0xFF);
outputBuffer[d
// Enable
clock
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x8B;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
data
bits
low
byte
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x80;
outputBuffer[dwNumBytesToSend + +] = 0x1B;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
data
bits
high
byte
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x82;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
latency
timer
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x97;
outputBuffer[dwNumBytesToSend + +] = 0xFF;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
flow
control
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x85;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
Tx / Rx
LED
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x86;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
Tx / Rx
LED
polarity
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x9D;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
event
character
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x99;
outputBuffer[dwNumBytesToSend + +] = 0x00;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
error
character
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x9A;
outputBuffer[dwNumBytesToSend + +] = 0x00;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytes
                          // Set
reset
duration
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x98;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
read and write
timeout
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x9E;
outputBuffer[dwNumBytesToSend + +] = 0x01;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
modem
control
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x9C;
outputBuffer[dwNumBytesToSend + +] = 0x03;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
line
control
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x9B;
outputBuffer[dwNumBytesToSend + +] = 0x03;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
break
duration
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x9F;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
break
type
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x9F;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
divisor
latch
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x9F;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
flow
control
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x9F;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
data
bits
low
byte
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x9F;
outputBuffer[dwNumBytesToSend + +] = 0x00;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend,
           // Set
Baud
rate
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x86;
outputBuffer[dwNumBytesToSend + +] = (byte)(dwClockDivisor & 0xFF);
outputBuffer[dwNumBytesToSend + +] = (byte)((dwClockDivisor >> 8) & 0xFF);
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
data
control
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x85;
outputBuffer[dwNumBytesToSend + +] = 0x02;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
Tx / Rx
LED
polarity
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x9D;
outputBuffer[dwNumBytesToSend + +] = 0x01;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
data
bits
low
byte
dwNumBytesToSend = 0;
outputBuffer[dwNumBytesToSend + +] = 0x80;
outputBuffer[dwNumBytesToSend + +] = 0x0B;
ftStatus = ftHandle.Write(outputBuffer, dwNumBytesToSend, ref
dwNumBytesSent);

// Set
data
bits
high
byte
dwNumBytesToSend

