# your_package_name/your_package_name/keyboard_teleop.py

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

import sys
import select
import termios
import tty

msg = """
Control Your Robot!
---------------------------
Moving around:
        w
   a    s    d
        x

w/x : increase/decrease linear velocity (X)
a/d : increase/decrease angular velocity (Z)

anything else : stop

CTRL-C to quit
"""

moveBindings = {
    'w':(1,0),
    's':(-1,0),
    'a':(0,1),
    'd':(0,-1),
    'x':(0,0),
}


class KeyboardTeleop(Node):

    def __init__(self):
        super().__init__('keyboard_teleop')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timeout = 0.1
        self.speed = 0.5
        self.turn = 0.5
        self.settings = termios.tcgetattr(sys.stdin)
        
    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def run(self):
        try:
            print(msg)
            while True:
                key = self.getKey()
                if key in moveBindings.keys():
                    x, th = moveBindings[key]
                    twist = Twist()
                    twist.linear.x = x * self.speed
                    twist.angular.z = th * self.turn
                    self.publisher_.publish(twist)
                if (key == '\x03'):
                    break

        except Exception as e:
            print(e)

        finally:
            twist = Twist()
            twist.linear.x = 0
            twist.angular.z = 0
            self.publisher_.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    keyboard_teleop = KeyboardTeleop()

    try:
        keyboard_teleop.run()
    finally:
        keyboard_teleop.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

