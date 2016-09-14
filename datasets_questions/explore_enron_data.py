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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print ("Number of people:", len(enron_data))
print ("Number of features:", len(enron_data['GARLAND C KEVIN']))
print ("Number of POIs:", sum(1 for x in enron_data if enron_data[x]['poi'] == 1))
print ("James Prentice stock value:", enron_data["PRENTICE JAMES"]['total_stock_value'])
print ("Wesley Colwell email:", enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])
print ("Jeffrey K Skilling stock options exercised:", enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])
print ("Jeffrey K Skilling total payment:", enron_data["SKILLING JEFFREY K"]['total_payments'])
print ("Kenneth Lay total payment:", enron_data["LAY KENNETH L"]['total_payments'])
print ("Andrew Fastow total payment:", enron_data["FASTOW ANDREW S"]['total_payments'])
print ("Number of quantified salaries:", sum(1 for x in enron_data if enron_data[x]['salary'] != 'NaN'))
print ("Number of known emails:", sum(1 for x in enron_data if enron_data[x]['email_address'] != 'NaN'))
print ("NaN total payments:", sum(1 for x in enron_data if enron_data[x]['total_payments'] == 'NaN'))
print ("Number of records:", len(enron_data))
print ("Percentage of people in the dataset have NaN total payments:", sum(1 for x in enron_data if enron_data[x]['total_payments'] == 'NaN') * 1.0 / len(enron_data))
print ("Percentage of POI in the dataset have NaN total payments:", sum(1 for x in enron_data if enron_data[x]['total_payments'] == 'NaN' and enron_data[x]['poi'] == True) * 1.0 / len(enron_data))