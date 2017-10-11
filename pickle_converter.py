import pickle
'''
There is a protocol mismatch between the pickle used in python 2 and python 3.
To encounter this problem, we have this pickle_converter which translates
pickle entries to new group.
'''

pickle_in = open('english_without_processing.pickle','rb')
mlp=pickle.load(pickle_in)

with open('english_without_processing_test.pickle','wb') as f:
	pickle.dump(mlp,f, protocol=2)
