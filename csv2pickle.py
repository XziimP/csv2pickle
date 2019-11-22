import pickle
import pandas as pd

example = pd.read_csv('C:\\Users\\Rishabh\\Desktop\\New folder\\New folder\\bank-additional.csv')
#pd.read_csv('C:\\Users\\Rishabh\\Desktop\\New folder\\New folder\\n.csv') 
pickle_out = open("C:\\Users\\Rishabh\\Desktop\\New folder\\New folder\\dict.pickle","wb")
pickle.dump(example,pickle_out)
pickle_out.close()

pickle_in = open("C:\\Users\\Rishabh\\Desktop\\New folder\\New folder\\dict.pickle","rb")
example_dict = pickle.load(pickle_in)

print(example_dict)
