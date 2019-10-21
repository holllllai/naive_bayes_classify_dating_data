import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

INPUT_FILE = '../assg2_release/dating.csv'
df = pd.read_csv(INPUT_FILE)


list_partner = ['attractive_partner','sincere_partner','intelligence_parter','funny_partner','ambition_partner','shared_interests_partner']

print('Number of distinct values for attractive_partner: ',len(df['attractive_partner'].unique()))
print('Number of distinct values for sincere_partner: ',len(df['sincere_partner'].unique()))
print('Number of distinct values for intelligence_partner: ',len(df['intelligence_parter'].unique()))
print('Number of distinct values for funny_partner: ',len(df['funny_partner'].unique()))
print('Number of distinct values for ambition_partner: ',len(df['ambition_partner'].unique()))
print('Number of distinct values for shared_interests_partner: ',len(df['shared_interests_partner'].unique()))

x_attractive = []
y_attractive = []
x_sincere =[]
y_sincere = []
x_intelligence = []
y_intelligence = []
x_funny = []
y_funny =[]
x_ambition = []
y_ambition = []
x_shared_interest = []
y_shared_interest = []

for value in df['attractive_partner'].unique():
	success_rate = len(df[(df['attractive_partner']==float(value)) & (df['decision']==1)])/len(df[df['attractive_partner']==value])
	print('The success rate given', value, 'in attractive_partner is', success_rate )
	x_attractive.append(value)
	y_attractive.append(success_rate)
for value in df['sincere_partner'].unique():
	success_rate = len(df[(df['sincere_partner']==float(value)) & (df['decision']==1)])/len(df[df['sincere_partner']==value])
	print('The success rate given', value, 'in sincere_partner is', success_rate )
	x_sincere.append(value)
	y_sincere.append(success_rate)
for value in df['intelligence_parter'].unique():
	success_rate = len(df[(df['intelligence_parter']==float(value)) & (df['decision']==1)])/len(df[df['intelligence_parter']==value])
	print('The success rate given', value, 'in intelligence_partner is', success_rate )
	x_intelligence.append(value)
	y_intelligence.append(success_rate)

for value in df['funny_partner'].unique():
	success_rate = len(df[(df['funny_partner']==float(value)) & (df['decision']==1)])/len(df[df['funny_partner']==value])
	print('The success rate given ',value,'in funny partner is', success_rate )
	x_funny.append(value)
	y_funny.append(success_rate)
for value in df['ambition_partner'].unique():
	success_rate = len(df[(df['ambition_partner']==float(value)) & (df['decision']==1)])/len(df[df['ambition_partner']==value])
	print('The success rate given ',value,'in ambition partner is', success_rate )
	x_ambition.append(value)
	y_ambition.append(success_rate)

for value in df['shared_interests_partner'].unique():
	success_rate = len(df[(df['shared_interests_partner']==float(value)) & (df['decision']==1)])/len(df[df['shared_interests_partner']==value])
	print('The success rate given ',value,' in shared interest partner is', success_rate )
	x_shared_interest.append(value)
	y_shared_interest.append(success_rate)


making scatter plot
plt.figure(figsize=(10,5))
plt.scatter(x_attractive,y_attractive)
plt.title('success rate given a partner score for the attribute attractive')
plt.xlabel('value')
plt.ylabel('success rate')
plt.savefig('../assignment2_solution/attractive_sr.png')

plt.figure(figsize=(10,5))
plt.scatter(x_sincere,y_sincere)
plt.title('success rate given a partner score for the attribute sincere')
plt.xlabel('value')
plt.ylabel('success rate')
plt.savefig('../assignment2_solution/sincere_sr.png')

plt.figure(figsize=(10,5))
plt.scatter(x_intelligence,y_intelligence)
plt.title('success rate given a partner score for the attribute intelligence')
plt.xlabel('value')
plt.ylabel('success rate')
plt.savefig('../assignment2_solution/intelligence_sr.png')

plt.figure(figsize=(10,5))
plt.scatter(x_ambition,y_ambition)
plt.title('success rate given a partner score for the attribute ambition')
plt.xlabel('value')
plt.ylabel('success rate')
plt.savefig('../assignment2_solution/ambition_sr.png')

plt.figure(figsize=(10,5))
plt.scatter(x_funny,y_funny)
plt.title('success rate given a partner score for the attribute funny')
plt.xlabel('value')
plt.ylabel('success rate')
plt.savefig('../assignment2_solution/funny_sr.png')

plt.figure(figsize=(10,5))
plt.scatter(x_shared_interest,y_shared_interest)
plt.title('success rate given a partner score for the attribute shared interest')
plt.xlabel('value')
plt.ylabel('success rate')
plt.savefig('../assignment2_solution/shared_interest_sr.png')
