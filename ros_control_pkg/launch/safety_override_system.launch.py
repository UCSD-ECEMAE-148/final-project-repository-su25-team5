from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros_control_pkg',
            executable='donkey_bridge_node',
            name='donkey_bridge',
            output='screen'
        ),
        Node(
            package='ros_control_pkg',
            executable='safety_override_node',
            name='safety_override',
            output='screen'
        ),
        Node(
            package='ros_control_pkg',
            executable='smart_avoid_node',
            name='smart_avoid',
            output='screen'
        ),
    ])
