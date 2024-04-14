# ROS 2 Talker-Listener Example

This is a simple ROS 2 example project demonstrating the concept of publisher and subscriber nodes.

## Talker Node

The talker node (`talker.py`) publishes messages to the `/chatter` topic at a regular interval. Each message contains a string with the format "This is talker [count]".

## Listener Node

The listener node (`listener.py`) subscribes to the `/chatter` topic and prints the received messages to the console.

## Usage

To use this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone git@github.com:Shubhankar2003/Talker_Listener_ROS2.git
    ```

2. Build the project:

    ```bash
    cd your_repo
    colcon build
    ```

3. Source the setup files:

    ```bash
    . install/setup.bash
    ```

4. Run the talker node:

    ```bash
    ros2 run talker_listener talker
    ```

5. In another terminal, run the listener node:

    ```bash
    ros2 run talker_listener listener
    ```

You should now see the talker node publishing messages and the listener node receiving and printing those messages.

## Dependencies

- ROS 2
- Python 3
- rclpy
- std_msgs
