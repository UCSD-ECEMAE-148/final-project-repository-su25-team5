#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.executors import SingleThreadedExecutor

class ROS2BridgePart():
    """
    ROS2 + DonkeyCar part combined.
    Subscribes to /cmd_vel2 (String) and exposes
    update() returning (steering, throttle).
    """
    def __init__(self):
        if not rclpy.ok:
            rclpy.init()

        self.node = Node('donkey_subscriber')
        self.steering = 0.0
        self.throttle = 0.0

        self.node.create_subscription(
            String,
            '/cmd_vel2',
            self.callback,
            10
        )

        self.executor = rclpy.executors.SingleThreadedExecutor()
        self.executor.add_node(self.node)

        # Run the executor in a background thread
        self.thread = Thread(target=self.executor.spin, daemon=True)
        self.thread.start()
        self.get_logger().info(f"{name} node started.")

    def cmd_vel_callback(self, msg):
        """Parse String message: 'THROTTLE:<value>,STEERING:<value>'"""
        try:
            parts = msg.data.split(',')
            self.throttle = float(parts[0].split(':')[1])
            self.steering = float(parts[1].split(':')[1])
        except Exception as e:
            self.get_logger().error(f"Failed to parse /cmd_vel2: {msg.data} ({e})")

    def update(self):
        """Called by DonkeyCar vehicle loop"""
        return self.steering, self.throttle

    def shutdown(self):
        """Clean shutdown"""
        self.executor.shutdown()
        self.destroy_node()

# -------------------------------
# Standalone ROS2 Entry Point
# -------------------------------
def main(args=None):
    rclpy.init(args=args)
    node = DonkeyBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
