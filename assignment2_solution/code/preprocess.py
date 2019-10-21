import pandas as pd
INPUT_FILE = '../assg2_release/dating-full.csv'
dating_full = pd.read_csv(INPUT_FILE)
OUTPUT_FILE = '../assg2_release/dating.csv'
'''
I. Preprocessing
'''
#(i) The format of values in some columns of the dataset is not unified. Strip the surrounding quotes in the values for columns race, 
#race o and field (e.g., ‘Asian/Pacific Islander/Asian- American’ → Asian/Pacific Islander/Asian-American), 
#count how many cells are changed after this pre-processing step, and output this number.

print("quotes removed from ", len(dating_full[dating_full['race'].str.contains("'")])+len(dating_full[dating_full['race_o'].str.contains("'")])+len(dating_full[dating_full['field'].str.contains("'")]), "cells")


dating_full['race'] = dating_full['race'].str.replace("'", "")
dating_full['race_o'] = dating_full['race_o'].str.replace("'", "")
dating_full['field'] = dating_full['field'].str.replace("'", "")

#(ii)Convert all the values in the column field to lowercase if they are not already in lowercases (e.g., Law → law). 
#Count the number of cells that are changed after this pre-processing step, and output this number.
print(len(dating_full[dating_full['field'].str.contains(r"[A-Z]")]),"Standardized field cells to lower case")
dating_full['field']=dating_full['field'].str.lower()

#Use label encoding to convert the categorical values in columns gender, race, race o and field 
#to numeric values start from 0. The process of label encoding works by mapping each categorical value 
#of an attribute to an integer number between 0 and nvalues − 1 where nvalues is the number of distinct values 
#for that attribute. Sort the values of each categorical attribute lexicographically/alphabetically before you 
#start the encoding process. You are then asked to output the mapped numeric values for ‘male’ in the gender column, 
#for ‘European/Caucasian-American’ in the race column, for ‘Latino/Hispanic American’ in the race o column,
# and for ‘law’ in the field column.
dating_full['gender'] = dating_full['gender'].astype('category')
dating_full['race'] = dating_full['race'].astype('category')
dating_full['race_o'] = dating_full['race_o'].astype('category')
dating_full['field'] = dating_full['field'].astype('category')

d_gender = dict(enumerate(dating_full['gender'].cat.categories)) #creating dictionary for categories and their labels i.e: {0:"female",1:'male'}
d_gender = {v: k for k, v in d_gender.items()} #inverse dictionary key,value pairs for later access. i.e: ("female":0, "male":1)
d_race = dict(enumerate(dating_full['race'].cat.categories))
d_race = {v: k for k, v in d_race.items()}
d_raceo = dict(enumerate(dating_full['race_o'].cat.categories))
d_raceo = {v: k for k, v in d_raceo.items()}
d_field = dict(enumerate(dating_full['field'].cat.categories))
d_field = {v: k for k, v in d_field.items()}


dating_full['race'] = dating_full['race'].cat.codes
dating_full['gender'] = dating_full['gender'].cat.codes
dating_full['race_o'] = dating_full['race_o'].cat.codes
dating_full['field'] = dating_full['field'].cat.codes

print('Value assigned for male in column gender:', d_gender['male'])
print('Value assigned for European/Caucasian-American in column race: ',d_race['European/Caucasian-American'])
print('Value assigned for Latino/Hispanic American in column race o: ', d_raceo['Latino/Hispanic American'])
print('Value assigned for law in column field: ', d_field['law'])

#(iv)Normalization
list_pref_o = ['pref_o_attractive', 'pref_o_sincere', 'pref_o_intelligence', 'pref_o_funny','pref_o_ambitious','pref_o_shared_interests']
list_importance = ['attractive_important','sincere_important','intelligence_important','funny_important','ambition_important','shared_interests_important']

dating_full['total_pref_o'] = dating_full[list_pref_o[0]]+ dating_full[list_pref_o[1]]+dating_full[list_pref_o[2]]+dating_full[list_pref_o[3]]+dating_full[list_pref_o[4]]+dating_full[list_pref_o[5]]
for item in list_pref_o:
	dating_full[item] = dating_full[item]/dating_full['total_pref_o']

dating_full['total_importance'] = dating_full[list_importance[0]]+dating_full[list_importance[1]]+dating_full[list_importance[2]]+dating_full[list_importance[3]]+dating_full[list_importance[4]]+dating_full[list_importance[5]]
for item in list_importance:
	dating_full[item] = dating_full[item]/dating_full['total_importance']

# dating_full['total_partner'] = dating_full[list_partner[0]]+dating_full[list_partner[1]]+dating_full[list_partner[2]]+dating_full[list_partner[3]]+dating_full[list_partner[4]]+dating_full[list_partner[5]]
# for item in list_partner:
# 	dating_full[item] = dating_full[item]/dating_full['total_partner']

dating_full = dating_full.drop(columns=['total_pref_o', 'total_importance'])

for item in list_importance:
	print('Mean of ' + str(item) + ':' , round(dating_full.loc[:,item].mean(),2))
for item in list_pref_o:
	print('Mean of ' + str(item) + ':' , round(dating_full.loc[:,item].mean(),2))

dating_full.to_csv(OUTPUT_FILE)

