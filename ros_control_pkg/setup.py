from setuptools import setup
import os
from glob import glob

package_name = 'ros_control_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Zhenyu Jiang',
    maintainer_email='zhj014@ucsd.edu',
    description='ROS2 control package with DonkeyCar bridge, safety override, and smart avoidance nodes',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'donkey_bridge_node = ros_control_pkg.donkey_bridge:main',
            'safety_override_node = ros_control_pkg.safety_override:main',
            'smart_avoid_node = ros_control_pkg.smart_avoid:main',
        ],
    },
)
