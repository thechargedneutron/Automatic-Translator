import matplotlib.pyplot as plt
import numpy as np

def show(a):
	'''
	Represents an input vector of size 1024 into corresponding 32X32 image.
	'''
	a_ = np.array(a)
	X_image = a_.reshape(32, 32)
	plt.axis('off')
	plt.imshow(X_image, cmap=plt.get_cmap('gray'))
	plt.show()


