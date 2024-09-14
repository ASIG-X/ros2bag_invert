# ros2bag_invert
ros2bag_invert supports inverting ROS2 bag files with custom messages to ROS bag files. 
## Dependency
System dependencies (tested on Ubuntu 22.04)
* [rosbags](https://gitlab.com/ternaris/rosbags) (tested with version 0.10.3)
```
sudo pip3 install rosbags
```
## Usage
To use this plugin, please follow the steps below.

1. Clone the repository
```
git clone https://github.com/ASIG-X/ros2bag_invert
```
2. Define the custom message types of the source ros2bag file that need to be converted and put the files under the main directory. Please check folder `livox_ros_driver2` as an example.
3. Run the following command in the terminal
```
cd ros2bag_invert
python3 invertBag/main.py -src /path/to/source/bag/file/ -dst /path/to/destination/bag/file/bag_name.bag -msg_paths /path/to/custom/messages/message_name.msg
# e.g., python3 invertBag/main.py -src ~/Documents/testbag/ -dst ./testbag.bag -msg_paths ./livox_ros_driver2/msg/CustomPoint.msg  ./livox_ros_driver2/msg/CustomMsg.msg
```
## Contributors
Ziyu Cao (email: ziyu.cao@liu.se)

Kailai Li (email: kailai.li@rug.nl)
## License
The source code is released under [GPLv3](https://www.gnu.org/licenses/) license.

We are constantly working on improving our code. For any technical issues, please contact Ziyu Cao (ziyu.cao@liu.se).
