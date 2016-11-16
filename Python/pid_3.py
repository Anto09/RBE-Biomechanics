#!/usr/bin/env python
 
import sys
import math
import numpy as np
import random
import matplotlib.pyplot as plt

class PID:
    kp = 0.4
    kd = 0.5

    derivator = 0.0
    error_t = 0.0
    error_td = 0.0
 
    p_value = 0.0
    d_value = 0.0
    i_value = 0.0

    dist_array = []
    cur_t_arr = []
    tar_t_arr = []


    cur_td = 0.0
    tar_td = 0.0

    cur_t = 0.0
    tar_t = 0.0

    l1 = 0.1
    m1 = 3.0
    r1 = 0.05

    max_torque = -99999999
 
    def target_angle_drv(self, idx):
        return -np.sin((np.pi/3.0) * float(idx) + np.pi/16.0) * (np.pi/3.0)
 
    def target_angle(self, idx):
        return (3.0/8.0) * np.pi + np.pi/8 * np.cos(float(idx) * (np.pi/3.0) + (np.pi/16.0))

    def calculate_arm_pos(self, theta):
        return [self.l1*np.cos(theta), self.l1*np.sin(theta)]

    def calc_error(self, pos1, pos2):
        return np.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2)

    def calc_torque(self):
        torque = (0.03*self.cur_td + 0.01) - (np.cos(self.cur_t) * 2.94)
        self.max_torque = max(self.max_torque, torque)

    def simulate(self, idx):
        self.tar_t = self.target_angle(idx)
        self.tar_td = self.target_angle_drv(idx)

        self.cur_td = self.update()
        self.cur_t += (self.cur_td)

        self.cur_t_arr.append(self.cur_t)
        self.tar_t_arr.append(self.tar_t)
        self.calc_torque()

        t_hand_pos = self.calculate_arm_pos(self.tar_t)
        c_hand_pos = self.calculate_arm_pos(self.cur_t)
        self.dist_array.append(self.calc_error(t_hand_pos, c_hand_pos))

    def update(self): #calculate new acceleration value
        self.error_t = self.tar_t - self.cur_t
        self.error_td = self.tar_td - self.cur_td
        self.p_value = self.kp * self.error_t
        self.d_value = self.kd * self.error_td
 

        PID = self.p_value + self.d_value
 
        return PID
 
def main():
    p = PID()
    for i in range(0, 1000): #update every 50ms
        if (i > 0):
            p.simulate(i)
    print (max(p.dist_array))
    print (p.max_torque)
    plt.plot(p.tar_t_arr, 'b')
    plt.plot(p.cur_t_arr, 'r')
    plt.plot(p.dist_array, 'g')
    plt.show()

 
if __name__ == "__main__":
     main()

