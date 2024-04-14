#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):

    def __init__(self):
        super().__init__("talker")
        self.i = 0
        
        self.pub = self.create_publisher(
            String,
            "chatter",
            10
        ) 

        self.create_timer(1.0, self.timer_callback)
        
    def timer_callback(self):
        msg = String()
        msg.data = f"This is talker {self.i}"
        self.pub.publish(msg)
        self.i += 1
        self.get_logger().info(f"Publishing: {msg.data}")


def main(args = None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
