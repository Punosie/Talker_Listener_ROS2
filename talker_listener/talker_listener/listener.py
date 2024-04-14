#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(String, "/chatter", self.sub_callback, 10 )

    def sub_callback(self, msg:String):
        self.get_logger().info(f"I listen: \"{msg.data}\" ")



def main(args = None):
    rclpy.init(args = args)
    node = Listener()
    rclpy.spin(node)
    rclpy.shutdown()
