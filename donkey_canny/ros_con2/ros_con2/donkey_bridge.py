# the node that orginally subscribes to /cmd_vel2 and updates shared data in the manage.py from donkey car
# BUG - it can't run in ros and manage.py at the same time, because both of them will call rclpy.init()
# solution - creating a custom part in donkey car that subscribes to /cmd_vel2 and updates the angle and throttle directly

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

shared_data = {"angle": 0.0, "throttle": 0.0}

class DonkeyBridgeNode(Node):
    def __init__(self):
        super().__init__('donkey_bridge_node')
        self.sub = self.create_subscription(
            String,
            '/cmd_vel2',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f"Publishing angle: {msg.data}")
        try:
            parts = msg.data.split(',')
            throttle = float(parts[0].split(':')[1])
            steering = float(parts[1].split(':')[1])
            shared_data["throttle"] = throttle
            shared_data["angle"] = steering
        except Exception as e:
            self.get_logger().error(f"Parse error: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = DonkeyBridgeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
