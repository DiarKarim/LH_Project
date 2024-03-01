import socket
import time 

UDP_IP = "127.0.0.1"
UDP_PORT = 8008

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(0)  # Set socket to non-blocking mode

try:
    while True:
        try:
            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            message = data.decode('utf-8').split('\x00', 1)[0]
            print("received message:", message)
        except BlockingIOError:
            # No data received, proceed with other tasks
            # print("No data received!!")
            pass

        print("Rest of code!!")

        # Here you can continue with the rest of your loop, for example, reading from a serial port
        # Example: print("Doing other tasks")
        # Remember to include a short sleep to prevent this loop from consuming too much CPU
        time.sleep(0.01)  # Adjust the sleep time as needed for your application

except KeyboardInterrupt:
    sock.close()







# try:
#     while True:
#         data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#         # Decode byte data to string using UTF-8 encoding, then split by null byte and take the first part
#         message = data.decode('utf-8').split('\x00', 1)[0]
#         print("Experimental_Phases:", message)
# except KeyboardInterrupt:
#     sock.close()
#     pass



# try:
#     while True:
#         data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#         print("received message: %s" % data)
# except KeyboardInterrupt:
#     sock.close()
#     pass


# import serial
# import pandas as pd
# import matplotlib.pyplot as plt
# from datetime import datetime, timedelta
# import json

# # path = "C:/Users/Monter/Projects/LH_Project/Data/"
# path = "C:/Users/VR-Lab/Documents/Projects/LH_Project/Data/"

# # User-defined settings
# Participant_ID = input("Enter Participant ID: ")
# Condition = input("Enter Condition: ")
# Trial = input("Enter Trial: ")

# # Setup for serial communication
# ser = serial.Serial('COM6', 115200, timeout=1)

# # Plot setup
# plt.ion()  # Interactive mode on for dynamic updating of plot
# fig, ax = plt.subplots()
# lines = {'heart_rate': ax.plot([], [], 'r-', label='Heart Rate')[0],
#          'gsr_response': ax.plot([], [], 'g-', label='GSR Response')[0]}
# ax.legend()
# ax.set_xlabel('Time (s)')
# ax.set_ylabel('Readings')

# # DataFrame to store the data
# data = pd.DataFrame(columns=['heart_rate', 'gsr_response', 'time'])

# # Function to update the plot
# def update_plot():
#     if not data.empty:
#         lines['heart_rate'].set_data(data['time'], data['heart_rate'])
#         lines['gsr_response'].set_data(data['time'], data['gsr_response'])
#         ax.relim()
#         ax.autoscale_view()
#         fig.canvas.draw()
#         fig.canvas.flush_events()

# # Start capturing data
# start_time = datetime.now()
# while (datetime.now() - start_time).seconds < 30:
#     line = ser.readline()
#     if line:
#         try:
#             val = line.decode("unicode_escape")
#             vals = val.split(',')
#             heart_rate, gsr_response = map(int, vals[:2]) 
#             elapsed_time = (datetime.now() - start_time).total_seconds()
#             tmpDF = pd.DataFrame({'heart_rate': [heart_rate], 
#                                   'gsr_response': [gsr_response], 
#                                   'time': [elapsed_time]})
#             data = pd.concat([data, tmpDF])

#             if len(data) % 10 == 0:
#                 update_plot()
#         except ValueError:
#             pass  # Ignore malformed data

# # Closing serial port
# ser.close()

# # Adding extra columns
# data['Participant_ID'] = Participant_ID
# data['Condition'] = Condition
# data['Trial'] = Trial

# # Save to JSON
# current_time = datetime.now().strftime("%d%m%y_%H%M%S")
# filename = f"ptxid_{Participant_ID}_condition_{Condition}_trial_{Trial}_time_{current_time}.json"
# # data.to_json(path + filename, orient='records')

# # Convert DataFrame to a dictionary with column headers as keys and values as lists
# data_dict = {col: data[col].tolist() for col in data.columns}

# # Save this dictionary as JSON
# with open(path + filename, 'w') as file:
#     json.dump(data_dict, file)

# # Notify the user
# print(f"Data capture complete. Data saved to {filename}")