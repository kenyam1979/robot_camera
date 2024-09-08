import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class RobotCamera(Node):
    def __init__(self):
        super().__init__('robot_camera')

        self.publisher_ = self.create_publisher(Image, 'image', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_cb)

        self.cap = cv2.VideoCapture(0)
        self.br = CvBridge()

    def timer_cb(self):
        ret, frame = self.cap.read()
        if ret == True:
            dst = cv2.resize(frame, (160,120))
            self.publisher_.publish(self.br.cv2_to_imgmsg(dst))
            # print('Running....')


def main(args=None):
    rclpy.init(args=args)
    camera = RobotCamera()
    rclpy.spin(camera)

    camera.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

