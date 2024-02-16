from setuptools import find_packages, setup
import os

package_name = 'keyboard_teleop'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/keyboard_teleop.launch.py']),
        (os.path.join('share', package_name, 'model', 'truck03'), ['model/truck03/model.sdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='taisyu',
    maintainer_email='t_shiba117@yahoo.co.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'keyboard_teleop = keyboard_teleop.keyboard_teleop:main',
        ],
    },
)
