#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, LaserScan
from geometry_msgs.msg import Twist

# the idea of this node is to send command from ROS2 to donkey car
class DonkeyBridge(Node):

    def __init__(self, car=None):
        super().__init__('donkey_bridge')

        # save handle to DonkeyCar (if passed in from manage.py)
        self.car = car

        # Subscriber: listen for velocity commands from ROS
        self.cmd_vel_sub = self.create_subscription(
            Twist, 'cmd_vel', self.cmd_vel_callback, 10)

        # Timer to periodically publish sensor data
        timer_period = 0.1  # 10 Hz
        #self.timer = self.create_timer(timer_period, self.publish_sensors)

        self.get_logger().info("DonkeyBridge node started.")

    def cmd_vel_callback(self, msg):
        # Convert Twist -> DonkeyCar throttle + steering
        throttle = msg.linear.x
        steering = msg.angular.z

        if self.car:
            # Example: update your car actuators
            self.car.update_controls(throttle, steering)
        else:
            self.get_logger().warn("No DonkeyCar handle attached!")

    # def publish_sensors(self):
    #     # Example: publish dummy sensor data
    #     self.get_logger().info("Publishing sensors...")
    #     # You can add actual publishing here


def main(args=None):
    rclpy.init(args=args)
    node = DonkeyBridge()  # Or pass DonkeyCar object here later
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
