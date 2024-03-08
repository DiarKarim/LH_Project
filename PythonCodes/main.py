import serial
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import json
import time 
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 8008
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(0)  # Set socket to non-blocking mode


# path = "C:/Users/Monter/Projects/LH_Project/Data/"
path = "C:/Users/VR-Lab/Documents/Projects/LH_Project/Data/"

# User-defined settings
Participant_ID = input("Enter Participant ID: ")
Condition = input("Enter Condition: ")
Trial = input("Enter Trial: ")

# Setup for serial communication
ser = serial.Serial('COM6', 115200, timeout=1)

# Plot setup
plt.ion()  # Interactive mode on for dynamic updating of plot
fig, ax = plt.subplots()
lines = {'heart_rate': ax.plot([], [], 'r-', label='Heart Rate')[0],
         'gsr_response': ax.plot([], [], 'g-', label='GSR Response')[0]}
ax.legend()
ax.set_xlabel('Time (s)')
ax.set_ylabel('Readings')

# DataFrame to store the data
data = pd.DataFrame(columns=['heart_rate', 'gsr_response', 'time'])

# Function to update the plot
def update_plot():
    if not data.empty:
        lines['heart_rate'].set_data(data['time'], data['heart_rate'])
        lines['gsr_response'].set_data(data['time'], data['gsr_response'])
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        fig.canvas.flush_events()

# Start capturing data
start_time = datetime.now()
trialDuration = 600 # 10 mins
unreal_message = "startNow"
unreal_str = "startNow"

try:
    while (datetime.now() - start_time).seconds < trialDuration:
        line = ser.readline()
        if line:
            try:
                try:
                    msg, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
                    unreal_message = msg.decode('utf-8').split('\x00', 1)[0]
                    unreal_message = unreal_message[1:]
                    unreal_str = str(unreal_message)
                    print("Phase: ", unreal_str)

                except BlockingIOError: 
                    unreal_str = unreal_str
                    # No data received, proceed with other tasks
                    pass

                val = line.decode("unicode_escape")
                vals = val.split(',')
                heart_rate, gsr_response = map(int, vals[:2]) 
                elapsed_time = (datetime.now() - start_time).total_seconds()

                # print('Heartrate: ', unreal_str)

                tmpDF = pd.DataFrame({'heart_rate': [heart_rate], 
                                    'gsr_response': [gsr_response], 
                                    'time': [elapsed_time],
                                    'phase' : [unreal_str]})
                
                data = pd.concat([data, tmpDF])

                if len(data) % 100 == 0:
                    update_plot()

            except ValueError:
                pass  # Ignore malformed data

except KeyboardInterrupt:
    sock.close() # Closing the socket 
    ser.close() # Closing serial port

    # Adding extra columns
    data['Participant_ID'] = Participant_ID
    data['Condition'] = Condition
    data['Trial'] = Trial

    # Save to JSON
    current_time = datetime.now().strftime("%d%m%y_%H%M%S")
    filename = f"ptxid_{Participant_ID}_condition_{Condition}_trial_{Trial}_time_{current_time}.json"
    # data.to_json(path + filename, orient='records')

    # Convert DataFrame to a dictionary with column headers as keys and values as lists
    data_dict = {col: data[col].tolist() for col in data.columns}

    # Save this dictionary as JSON
    with open(path + filename, 'w') as file:
        json.dump(data_dict, file)

    # Notify the user
    print(f"Data capture complete. Data saved to {filename}")



# Adding extra columns
data['Participant_ID'] = Participant_ID
data['Condition'] = Condition
data['Trial'] = Trial

# Save to JSON
current_time = datetime.now().strftime("%d%m%y_%H%M%S")
filename = f"ptxid_{Participant_ID}_condition_{Condition}_trial_{Trial}_time_{current_time}.json"
# data.to_json(path + filename, orient='records')

# Convert DataFrame to a dictionary with column headers as keys and values as lists
data_dict = {col: data[col].tolist() for col in data.columns}

# Save this dictionary as JSON
with open(path + filename, 'w') as file:
    json.dump(data_dict, file)

# Notify the user
print(f"Data capture complete. Data saved to {filename}")