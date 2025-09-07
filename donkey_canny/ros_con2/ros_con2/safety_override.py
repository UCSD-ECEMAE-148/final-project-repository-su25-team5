
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import math
from geometry_msgs.msg import Twist



class FusionNode(Node):
    def __init__(self):
        super().__init__('fusion_node')
        self.lidar_status = None
        self.camera_status = None
        self.car_steering = 0.0
        self.car_acc = 0.5

        # Subscribers
        self.create_subscription(String, '/camera_status', self.camera_callback, 10)
        self.create_subscription(String, '/lidar_status', self.lidar_callback, 10)

        # Publisher
        # orginally publish to /cmd_vel2 for donkey_bridge.py to pick up, but somehow the custom part in donkey car does not work
        # so change to /cmd_vel to ensure the obstical avoidance works

        #self.pub = self.create_publisher(String, '/cmd_vel2', 10)
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def lidar_callback(self, msg):
        self.lidar_status = msg.data
        #self.get_logger().info(f"lidar: {msg.data}")
        self.make_decision()

    def camera_callback(self, msg):
        self.camera_status = msg.data
        self.make_decision()

    def make_decision(self):
        if self.lidar_status is None: #or self.camera_status is None:
            return  

        self.get_logger().info(f"lidar: {self.lidar_status}")

        # Rule 1: Safety first
        if self.lidar_status == "STOP":
            # decision = "STOP"
            self.car_acc = 0.0
            self.car_steering = 0.0

        # Rule 2: Pedestrian always STOP
        # BUG - camera can't run donkey car and ros at the same time, so disable this rule for now
        #elif "PEDESTRIAN" in self.camera_status.upper():
           # car_acc = 0.0
           # car_steering = 0.0

        # Rule 4: Obstacle left/right/slow down
        elif self.lidar_status in ["LEFT", "RIGHT"]:
            # if the car see stuff on the left
            if self.lidar_status == "LEFT":
                self.car_steering = 0.7
                self.car_acc = 0.3
            # if the car see stuff on the right
            else:
                self.car_steering = -0.7
                self.car_acc = 0.3
        else:
            self.car_steering = 0.0
            self.car_acc = 0.5

        # originally publish a string message to donkey_bridge.py
        #msg_out = String()
        # msg_out.data = f"STEERING:{self.car_steering},THROTTLE:{self.car_acc}"
        #msg_out.data = f"THROTTLE:{self.car_acc},STEERING:{self.car_steering}"
        
        msg_out = Twist()
        msg_out.linear.x = float(self.car_acc)
        msg_out.angular.z = float(self.car_steering)

        self.pub.publish(msg_out)
        self.get_logger().info(f"Published: THROTTLE={self.car_acc}, STEERING={self.car_steering}")
        # self.get_logger().info(f"Fusion Decision: {msg_out.data} "
        #                        f"(LIDAR={self.lidar_status}, CAMERA={self.camera_status})")


def main(args=None):
    rclpy.init(args=args)
    node = FusionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
