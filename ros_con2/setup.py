from setuptools import setup
import os
from glob import glob

package_name = 'ros_con2'

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
    maintainer='root',
    maintainer_email='djnighti@ucsd.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['donkey_bridge_node = ros_con2.donkey_bridge:main',
            'safety_override_node = ros_con2.safety_override:main',
            'smart_avoid_node = ros_con2.smart_avoid:main',
        ],
    },
)
