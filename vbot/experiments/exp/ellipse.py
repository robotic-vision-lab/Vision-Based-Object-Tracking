import numpy as np
from numpy import linalg as LA
from scipy.spatial.transform import Rotation as R

class Ellipse2D:
	def __init__(self, major_axis_len=1, minor_axis_len=1, center_coords=(0,0), rotation_angle=0):
		self.major_axis_len = major_axis_len
		self.minor_axis_len = minor_axis_len
		self.center_coords = center_coords
		self.rotation_angle = rotation_angle

		self._POINT_ENCLOSURE_TOLERANCE = 0.1

	def get_ellipse_params(self):
		return (
			self.major_axis_len,
			self.minor_axis_len,
			self.center_coords,
			self.rotation_angle
			)

	def enclose_points(self, points, tolerance=None):
		if tolerance is None:
			tolerance = self._POINT_ENCLOSURE_TOLERANCE

		# points passed will be of shape (-1, 1, 2)
		# reshape points to 2 x NUM_POINTS
		points = points.reshape(-1,2).T
		NUM_POINTS = points.shape[-1]

		# augment points with ones to have shape 3 x NUM_POINTS
		Q = np.concatenate((points, np.ones((1, NUM_POINTS))), axis=0)

		count = 1
		err = 1
		u  = np.ones((NUM_POINTS, 1)) / NUM_POINTS
		d = 2

		while err > tolerance:
			# X = Q . diag(u) . Q'
			# X = np.matmul(np.matmul(Q, np.diag(u.flatten())), Q.T)
			X = LA.multi_dot([Q, np.diag(u.flatten()), Q.T])

			# M = diag(Q' . X^-1 . Q)
			# M = np.diag(np.matmul(Q.T, np.matmul(np.linalg.pinv(X), Q)))
			M = np.diag(LA.multi_dot([Q.T, LA.pinv(X), Q]))

			_MAX_M = np.max(M)
			_ARG_MAX_M = np.argmax(M)

			step_size = (_MAX_M - d - 1) / ((d + 1) * (_MAX_M - 1))

			new_u = (1 - step_size) * u

			new_u[_ARG_MAX_M] += step_size

			err = LA.norm(new_u - u)

			count +=1 
			u = new_u

		# U = diag(u)
		U = np.diag(u.flatten())

		# A = (1/d) * ( (points . U . points') - (points . u . u.T . points.T) )
		# A = (1/d) * LA.pinv(( np.matmul(np.matmul(points, U), points.T) - np.matmul(np.matmul(points, u), np.matmul(u.T,points.T)) ))
		A = (1/d) * LA.pinv(LA.multi_dot([points, U, points.T]) - LA.multi_dot([points, u, u.T, points.T]))

		# compute SVD(A)
		_, Q, V = LA.svd(A)

		# rotate V matrix by 270. augment zeros to the right, then aug 0,0,1 to the bottom
		rot_V = np.rot90(V,3)
		rot_aug2_V = np.concatenate((rot_V, np.zeros((2,1))), axis=1)
		rot_aug3_V = np.concatenate((rot_aug2_V, np.array([[0,0,1]])), axis=0)

		# extract rotation from rotated augmented V
		rotation = R.from_matrix(rot_aug3_V)

		# update ellipse params
		self.minor_axis_len = 1 / (Q[0])**0.5
		self.major_axis_len = 1 / (Q[1])**0.5
		self.center_coords = tuple(map(int,np.matmul(points, u).flatten()))
		self.rotation_angle = rotation.as_euler('ZYX')[0]

		return self.get_ellipse_params()
