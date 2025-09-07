# the custom donkey part that bridges to ROS2
# BUG - does not work with manage.py yet, the overwrite to donkey car is not happening

import threading
import rclpy
from std_msgs.msg import String
import re

class ROS2BridgePart:
    def __init__(self):
        self.node = None   
        self.angle = 0.0
        self.throttle = 0.0
        self.lock = threading.Lock()

    def start(self):
        """Create the ROS2 Node after rclpy.init() has been called"""
        if self.node is None:
            from rclpy.node import Node

            class _BridgeNode(Node):
                def __init__(inner_self):
                    super().__init__('ros2_bridge_part')

                    # Subscribe to the cmd_val2 topic 
                    inner_self.sub_cmd = inner_self.create_subscription(
                        String,
                        '/cmd_val2',
                        self.cmd_callback,
                        10
                    )

                    inner_self.get_logger().info("ROS2BridgePart Node initialized and subscribed to /cmd_val2.")

            self.node = _BridgeNode()

    def cmd_callback(self, msg):
        """Parse string like 'THROTTLE:0.2,STEERING:0.5'"""
        try:
            match = re.search(r'THROTTLE:([-\d\.]+),STEERING:([-\d\.]+)', msg.data)
            if match:
                throttle_val = float(match.group(1))
                angle_val = float(match.group(2))
                with self.lock:
                    self.throttle = throttle_val
                    self.angle = angle_val
                if self.node:
                    self.node.get_logger().debug(f"Received -> angle: {angle_val:.3f}, throttle: {throttle_val:.3f}")
        except Exception as e:
            if self.node:
                self.node.get_logger().error(f"Failed to parse cmd_val2: {e}")

    def run(self):
        """this will overwrite the value in manage.py at the donkey car"""
        with self.lock:
            return self.angle, self.throttle
