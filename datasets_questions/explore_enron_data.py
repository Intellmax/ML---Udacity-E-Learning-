#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_file = r"C:\Users\Maksym_Parats\PycharmProjects\Udacity\final_project\final_project_dataset.pkl"

# file transformation into unix
destination = r"C:\Users\Maksym_Parats\PycharmProjects\Udacity\final_project\final_project_unix_dataset.pkl"
content = ''
outsize = 0
with open(enron_file, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))
print("Done. Saved %s bytes." % (len(content) - outsize))

enron_data = open(destination, "rb")
full_data = pickle.load(enron_data, fix_imports=True)


#EDA

print ('Total people {}'.format(len(full_data.keys())))
print ('Number of features {}'.format(len(full_data['METTS MARK'])))

count = 0
for i in full_data:
    if full_data[i]['poi'] == True:
        count+=1
print ('Number of poi(people of interest) {}'.format(count))

with open(r'C:\Users\Maksym_Parats\PycharmProjects\Udacity\final_project\poi_names.txt', 'r') as poi_names:
    text = poi_names.read().split('\n')[2:-1]
    print (text)
    print ('Number of POIs {}'.format(len(text)))

#What is the total value of the stock belonging to James Prentice?
for i in full_data.keys():
    if i.startswith('P'):
        print (i)

print (full_data['PRENTICE JAMES']['total_stock_value'])

#How many email messages do we have from Wesley Colwell to persons of interest?
for i in full_data.keys():
    if i.startswith('C'):
        print (i)

print (full_data['COLWELL WESLEY']['from_this_person_to_poi'])

#What’s the value of stock options exercised by Jeffrey K Skilling?
for i in full_data.keys():
    if i.startswith('S'):
        print (i)

print (full_data['SKILLING JEFFREY K']['exercised_stock_options'])