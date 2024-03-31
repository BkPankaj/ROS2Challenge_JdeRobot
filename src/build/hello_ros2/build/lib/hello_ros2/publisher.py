import rclpy
from std_msgs.msg import String

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('publisher_node')
    publisher = node.create_publisher(String, 'chatter', 10)
    msg = String()
    msg.data = 'Hello! ROS2 is fun'

    while rclpy.ok():
        publisher.publish(msg)
        node.get_logger().info('Publishing: "%s"' % msg.data)
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
