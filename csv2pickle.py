import pickle
import pandas as pd

example = pd.read_csv('/home/sean/btc-address.csv')
#pd.read_csv('C:\\Users\\Bhushan\\Desktop\\New folder\\New folder\\n.csv') 
pickle_out = open("/home/sean/btc1.pickle","wb")
pickle.dump(example,pickle_out)
pickle_out.close()

pickle_in = open("/home/sean/btc1.pickle","rb")
example_dict = pickle.load(pickle_in)

print(example_dict)
