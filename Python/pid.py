#!/usr/bin/env python

import sys
import math
import numpy as np
import random

class PID:
	kp = 10.0
	kd = 5.0
	ki = 2.0
	 
	derivator = 0.0
	integrator = 0.0
	i_min = -500
	i_max = 500

	sp_curr_pos = 0.0 # xc(t-100ms)
	sp_curr_vel = 0.0 # xc(t-100ms)
	sp_curr_acc = 0.0 # xc(t-100ms)
	sp_prev_pos = 0.0 # xc(t)
	sp_prev_vel = 0.0 # vc(t)
	sp_prev_acc = 0.0 # ac(t)
	sp_next_acc = 0.0

	prev_pos = 0.0 # xc(t-100ms)
	prev_vel = 0.0 # vc(t-100ms)
	prev_acc = 0.0 # ac(t-100ms)
	current_pos = 0.0 # xc(t)
	current_vel = 0.0 # vc(t)
	current_acc = 0.0 # ac(t)

	error = 0.0

	p_value = 0.0
	d_value = 0.0
	i_value = 0.0

	def clamp_acc(self):
		if (np.fabs(self.current_acc) > 20.0):
			self.current_acc = np.sign(self.current_acc) * 20.0

	def distort_acc(self): #randomize the ac(t)
		r = random.uniform(0.8, 1.0)
		self.current_acc = r * self.current_acc

	def calc_delayed_acc(self):
		self.prev_acc = (self.current_vel - self.prev_vel)/100.00

	def calc_vel(self):
		self.current_vel += (self.current_acc) * 100.00

	def calc_pos(self):
		self.current_pos += (self.current_vel * 100.00) + (0.5 * self.current_acc * (100.00**2))

	def simulate(self, idx, set_points):
		#calculate positions, velocities, and accelerations here

		####### set point calculation #######

		self.sp_prev_pos = self.sp_curr_pos
		self.sp_curr_pos = 	set_points[idx]

		if (idx < len(set_points)):
			self.sp_prev_vel = self.sp_curr_vel
			self.sp_curr_vel = self.sp_curr_vel + (self.sp_prev_acc * 100.00)
			self.sp_prev_acc = self.sp_curr_acc
			self.sp_curr_acc = self.sp_next_acc
			if (idx + 1 < len(set_points)):
				self.sp_next_acc = ((set_points[idx+1] - self.sp_curr_pos)/100.00 - self.sp_curr_vel) / 100.00

		####### current value calculation #######

		self.prev_pos = self.current_pos
		self.current_pos += (self.current_vel * 100.00) + (0.5 * self.current_acc * (100.00**2))
		self.prev_vel = self.current_vel
		self.current_vel += self.current_acc * 100.00
		self.prev_acc = self.current_acc
		self.current_acc = self.update()
		self.clamp_acc()
		self.distort_acc()

		print 'new acceleration', self.current_acc
		print 'new velocity', self.current_vel
		print 'new positions', self.current_pos

		# assume applied 


	# set point and current value are positions
	# calculate target and desired accelerations

	def update(self): #calculate new acceleration value
		self.error = self.sp_curr_acc - self.current_acc
		print 'error', self.error

		self.p_value = self.kp * self.error
		self.d_value = self.kd * (self.error - self.derivator)
		self.derivator = self.error

		self.integrator += self.error

		self.integrator = min(self.integrator, self.i_max)
		self.integrator = max(self.integrator, self.i_min)

		self.i_value = self.integrator * self.ki 
		PID = self.p_value + self.i_value + self.d_value


		raw_input('press enter to continue')
		return PID

def main(set_points):
	r = len(set_points);
	p = PID()
	for i in range(0, r+1):
		if (i > 0): #simulate delay
			p.simulate(i-1, set_points)
		print 'target_pos', set_points[i]
		print 'current_pos', p.current_pos

if __name__ == "__main__":

	i = 0
	set_points_1 = [0.0, 0.0, 0.2, 0.6, 1.7, 2.6, 3.1, 4.6, 3.9, 3.5, 2.4, 2.9, 1.4, 1.7, 4.5, 5.7, 6.5, 7.8, 8.2, 8.4, 8.5, 6.1, 5.4, 4.9, 4.1, 4.0, 3.8, 5.2, 5.6, 5.5, 2.3]
	set_points_2 = [1.1, 0.2, 0.4, 0.5, 0.1, 0.3, 0.7, 1.9, 3.7, 5.2, 7.9, 9.8, 6.2, 4.8, 3.0, 2.0, 1.3, 0.5, 0.3, 0.4, 0.6, 0.8, 1.8, 3.5, 5.1, 7.8, 9.4, 9.6, 9.7, 8.9, 1.1]

	# while (i != 1 or 1 != 0):
	# 	try:
	# 	    i=int(raw_input('Input:'))
	# 	    print i
	# 	except ValueError:
	# 	    print "Not a number"

	print 'calling'
	if (i == 0):
		main(set_points_1)
	else:
		main(set_points_2)