# donkey_bridge_node.py
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
        try:
            data = json.loads(msg.data)
            shared_data["angle"] = data.get("angle", 0.0)
            shared_data["throttle"] = data.get("throttle", 0.0)
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
