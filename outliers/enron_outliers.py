#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_unix_dataset.pkl", "rb"), fix_imports=True )
features = ["salary", "bonus"]
data_dict.pop("TOTAL",0)
data = featureFormat(data_dict, features)
print (data)

#find the biggest outlier
temp=sorted(data,key=lambda dat:dat[0], reverse=True)
max_sal= temp[0][0]
# print (temp)
# print (max_sal)
# print (data_dict)
#print max_sal
for key, value in data_dict.items():
    sal=value['salary']
    #print sal
    if sal == max_sal:
        print ('Max Salary={} is for the KEY={}'.format(sal,key))
        break

#find the biggest 4 outlier people names
for k,v in data_dict.items():
    salary=float(v.get('salary'))
    bonus=float(v.get('bonus'))
    if(salary>1000000 and bonus>=5000000):
        print(k)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


