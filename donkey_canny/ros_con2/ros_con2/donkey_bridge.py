#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


# -------------------------------
# ROS2 Node (subscribes to /cmd_vel2)
# -------------------------------
class DonkeyBridge(Node):
    def __init__(self, car=None):
        super().__init__('donkey_bridge')

        # save handle to DonkeyCar (if passed in from manage.py)
        self.car = car
        self.steering = 0.0
        self.throttle = 0.0

        # Subscriber: listen for velocity commands from ROS
        self.create_subscription(
            String, '/cmd_vel2', self.cmd_vel_callback, 10
        )

        self.get_logger().info("DonkeyBridge node started.")

    def cmd_vel_callback(self, msg):
        # Convert String -> DonkeyCar throttle + steering
        try:
            data = msg.data.split(',')
            self.throttle = float(data[0].split(':')[1])
            self.steering = float(data[1].split(':')[1])
            self.get_logger().info(
                f"Received cmd_vel: throttle={self.throttle}, steering={self.steering}"
            )
        except Exception as e:
            self.get_logger().error(f"Bad /cmd_vel2 format: {msg.data} ({e})")


# -------------------------------
# DonkeyCar Part Wrapper
# -------------------------------
class ROS2BridgePart:
    def __init__(self):
        rclpy.init(args=None)
        self.node = DonkeyBridge()
        from rclpy.executors import SingleThreadedExecutor
        self.executor = SingleThreadedExecutor()
        self.executor.add_node(self.node)

    def run(self):
        # Process ROS2 callbacks
        self.executor.spin_once(timeout_sec=0.01)

        # Return latest commands
        return self.node.steering, self.node.throttle

    def shutdown(self):
        self.executor.shutdown()
        self.node.destroy_node()
        rclpy.shutdown()


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
