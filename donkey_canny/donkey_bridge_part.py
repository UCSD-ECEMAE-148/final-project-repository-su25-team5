# donkey_bridge_part.py
import threading
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import re
from rclpy.executors import MultiThreadedExecutor

class ROS2BridgePart(Node):
    def __init__(self):
        super().__init__('ros2_bridge_part')

        # Latest command values
        self.angle = 0.0
        self.throttle = 0.0
        self.lock = threading.Lock()

        # Subscriber to the string topic
        self.sub_cmd = self.create_subscription(
            String,
            '/cmd_val2',   # your topic name
            self.cmd_callback,
            10
        )
        self.executor = rclpy.executors.MultiThreadedExecutor()
        self.executor.add_node(self)
        self._spin_thread = threading.Thread(target=self.executor.spin, daemon=True)
        self._spin_thread.start()
        self.get_logger().info("ROS2BridgePart initialized and subscribed to /cmd_val2.")

    def cmd_callback(self, msg):
        """Parse string like 'THROTTLE:0.2,STEERING:0.5'"""
        try:
            # Extract numbers using regex
            self.get_logger().info(msg.data)
            match = re.search(r'THROTTLE:([-\d\.]+),STEERING:([-\d\.]+)', msg.data)
            if match:
                throttle_val = float(match.group(1))
                angle_val = float(match.group(2))
                with self.lock:
                    self.throttle = throttle_val
                    self.angle = angle_val
                self.get_logger().debug(f"Received -> angle: {angle_val:.3f}, throttle: {throttle_val:.3f}")
        except Exception as e:
            self.get_logger().error(f"Failed to parse cmd_val2: {e}")

    def run(self):
        # Return latest command safely
        with self.lock:
            return self.angle, self.throttle

