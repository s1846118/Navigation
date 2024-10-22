from sensor_msgs.msg import NavSatFix
from nav_msgs.msg import Odometry
import rospy

import numpy
 
import utils

class my_navsat_transform:
    def __init__(self):
        self.origin = None
        self.seq = 0

    def set_origin(self, origin):
        self.origin = origin

    def transform_to_odometry(self, navsatfix_msg):
        y_coordinate = utils.get_distance_between_longlat(
            self.origin,
            utils.longlat_position(
                self.origin.longitude, # x
                navsatfix_msg.latitude # y
            )
        )
        if navsatfix_msg.latitude < self.origin.latitude:
            y_coordinate *= -1
        x_coordinate = utils.get_distance_between_longlat(
            self.origin,
            utils.longlat_position(
                navsatfix_msg.longitude, # x
                self.origin.latitude # y
            )
        )
        if navsatfix_msg.longitude < self.origin.longitude:
            x_coordinate *= -1
        # add gaussian noise with s.d. 1m
        noise = numpy.random.normal(loc=0, scale=0.2, size=2)
        # x_coordinate += noise[0]
        # y_coordinate += noise[1]
        self.seq += 1
        odom_msg = Odometry()
        odom_msg.header.seq = self.seq
        odom_msg.header.stamp = rospy.Time.now()
        odom_msg.header.frame_id = "map"
        odom_msg.child_frame_id = ""
        odom_msg.pose.pose.position.x = x_coordinate
        odom_msg.pose.pose.position.y = y_coordinate
        odom_msg.pose.pose.position.z = 0
        odom_msg.pose.pose.orientation.x = 0
        odom_msg.pose.pose.orientation.y = 0
        odom_msg.pose.pose.orientation.z = 0
        odom_msg.pose.pose.orientation.w = 0
        odom_msg.twist.twist.linear.x = 0
        odom_msg.twist.twist.linear.y = 0
        odom_msg.twist.twist.linear.z = 0
        odom_msg.twist.twist.angular.x = 0
        odom_msg.twist.twist.angular.y = 0
        odom_msg.twist.twist.angular.z = 0
        cov = [0 for i in range(36)]
        cov[0] = 0.2**2#(navsatfix_msg.position_covariance[0] * 100000)**2
        cov[7] = 0.2**2#(navsatfix_msg.position_covariance[4] * 100000)**2
        cov[14] = navsatfix_msg.position_covariance[8]
        odom_msg.pose.covariance = cov
        return odom_msg