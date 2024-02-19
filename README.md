# This is a ROS2 package for NeuraTruck GAZEBO simulation

* Terminal 1
```bash
mkdir -p neuratruck_ws/src && cd neuratruck_ws/src
git clone https://github.com/tstaisyu/keyboard_teleop_neuratruck.git
cd ..
colcon build
source install/setup.bash
ros2 launch keyboard_teleop keyboard_teleop.launch.py
```

* Terminal 2
```bash
source install/setup.bash
ros2 run keyboard_teleop keyboard_teleop
```