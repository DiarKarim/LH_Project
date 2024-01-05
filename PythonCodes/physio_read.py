import serial
import matplotlib.pyplot as plt
import time

ser = serial.Serial('COM5', 115200)
data_x = []
data_y = []
i = 0
start_time = time.time()
try:
    while True:
        line = ser.readline().decode().strip()
        if i % 10 == 0:
            data = line.split(',')
            data_x.append(float(data[0]))
            data_y.append(float(data[1]))
            time_elapsed = time.time() - start_time
            plt.subplot(2, 1, 1)
            plt.plot(time_elapsed, data_x, 'ro')
            plt.ylabel('x')
            plt.subplot(2, 1, 2)
            plt.plot(time_elapsed, data_y, 'bo')
            plt.ylabel('y')
            plt.xlabel('Time (s)')
            plt.show()
        print(line)
        i += 1
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting gracefully.")
