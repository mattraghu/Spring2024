import cv2
import numpy as np
import socket
import struct
import pickle

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a figure and a 3D axis
fig = plt.figure(figsize=(6, 6))

ax = fig.add_subplot(111, projection='3d')

# show lagend
ax.legend(['Voxels', 'Arrow', 'Start', 'Goal', 'Path']) 

# Set limits and labels
scale = .4
ax.set_xlim([10*scale, -20*scale])
#ax.set_zlim([-5*scale, 5*scale])
ax.set_zlim([5*scale, -5*scale])
ax.set_ylim([-1*scale, 5*scale])
ax.set_box_aspect([1,1,1])
ax.set_aspect('equal')
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Z Coordinate')
ax.set_zlabel('Y Coordinate')

fig2 = plt.figure(figsize=(6, 6))
ax2 = fig2.add_subplot(111)

fig3 = plt.figure(figsize=(6, 6))
# #add a histogram of point values
ax3 = fig3.add_subplot(111)
ax3.set_xlabel('Value')
ax3.set_ylabel('Frequency')
ax3.set_title('Histogram of Point Values')




# Enable interactive mode
plt.ion()

# Initial empty plot elements
scat = ax.scatter([], [], [], color='blue', s=5)  # Start with an empty scatter plot
arrow_lines = ax.plot([], [], [], color='purple')[0]  # Start with an empty arrow plot
start_point = ax.scatter([], [], [], color='green', s=100)  # Start with an empty start point plot
goal_point = ax.scatter([], [], [], color='red', s=100)  # Start with an empty goal point plot
path_line = ax.plot([], [], [], color='orange')[0]  # Start with an empty path plot

# Update function to be called in the loop
def update_plot(voxels, start, arrow_end, goal,path, img, points, colors):
    # # Filter voxels data based on the amount of points
    # x, y, z = zip(*voxels.keys())
    # colors = [voxels[(i, j, k)][2] for i, j, k in zip(x, y, z)]
    # colors = [(r/255, g/255, b/255) for r, g, b in colors]
    # # Update the scatter plot
    # scat._offsets3d = (x, z, y)
    # # scat.autoscale()
    # scat.set_color(colors)  # Directly setting RGB colors

    if points.shape == colors.shape:
        scat._offsets3d = (points[:,0], points[:,2], points[:,1])
        #normalize the colors
        colors = colors / 255
        scat.set_color(colors)

    
    # Update the arrow positions
    arrow_lines.set_xdata([start[0], arrow_end[0]])
    arrow_lines.set_ydata([start[2], arrow_end[2]])  # Swap y and z
    arrow_lines.set_3d_properties([start[1], arrow_end[1]])  # Swap y and z

    # Update the start point position
    start_point._offsets3d = ([start[0]], [start[2]], [start[1]])

    # Update the goal point position
    goal_point._offsets3d = ([goal[0]], [goal[2]], [goal[1]])

    # Update the path by adding the start point to the beggining (and get rid of the first point)
    path = np.array(path[:])
    path = np.vstack((start, path))

    path_line.set_xdata(path[:,0])
    path_line.set_ydata(path[:,2])
    path_line.set_3d_properties(path[:,1])

    ax2.imshow(img)


    # Update the histogram with the first value of the voxels items (omit 0)
    values = [voxels[key][0] for key in voxels.keys() if voxels[key][0] <= 100]
    ax3.hist(values, bins=10, color='blue', edgecolor='black')






# Create an INET, STREAMing socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '172.20.10.10'  # Adjust this to the server's IP
port = 9999

client_socket.connect((host_ip, port))
data = b""

# Receive data from the server
while True:
    # # Retrieve message size
    # while len(data) < struct.calcsize("L"):
    #     data += client_socket.recv(4096)

    # packed_msg_size = data[:struct.calcsize("L")]
    # data = data[struct.calcsize("L"):]
    # msg_size = struct.unpack("L", packed_msg_size)[0]

    # # Retrieve all data based on message size
    # while len(data) < msg_size:
    #     data += client_socket.recv(4096)

    # frame_data = data[:msg_size]
    # data = data[msg_size:]

    # # Extract frame
    # frame = cv2.imdecode(np.frombuffer(frame_data, dtype=np.uint8), 1)
    # cv2.imshow('Received Video', frame)

    # # Press 'Q' to exit!
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    # Receive the length of the data first
    data_len = struct.unpack("L", client_socket.recv(struct.calcsize("L")))[0]
    # Receive the serialized data
    data = b""
    while len(data) < data_len:
        packet = client_socket.recv(data_len - len(data))
        if not packet:
            break
        data += packet

    # Deserialize the received data back into a dictionary
    data_packed = pickle.loads(data)

    voxel_data = data_packed[0]
    path = data_packed[1]
    arrow_start = data_packed[2]
    arrow_end = data_packed[3]
    goal = data_packed[4]
    img = data_packed[5]
    points = data_packed[6]
    colors = data_packed[7]

    if not voxel_data:
        voxel_data = {(0,0,0):(0,0,(0,0,0))}


    # print(path)

    # Update the plot
    update_plot(voxel_data, arrow_start, arrow_end, goal, path, img, points, colors)

    # Redraw the plot
    fig.canvas.draw_idle()
    plt.pause(7)

    # send confirmation
    client_socket.sendall(b"Received")




client_socket.close()
cv2.destroyAllWindows()
