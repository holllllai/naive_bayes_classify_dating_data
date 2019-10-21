import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

INPUT_FILE = '../assg2_release/dating.csv'
df = pd.read_csv(INPUT_FILE)
df_female = df[df['gender']==0]
df_male = df[df['gender']==1]


list_pref_o = ['pref_o_attractive', 'pref_o_sincere', 'pref_o_intelligence', 'pref_o_funny','pref_o_ambitious','pref_o_shared_interests']
list_importance = ['attractive_important','sincere_important','intelligence_important','funny_important','ambition_important','shared_interests_important']
list_partner = ['attractive_partner','sincere_partner','intelligence_parter','funny_partner','ambition_partner','shared_interests_partner']

bar1 = []
bar2= []
for item in list_importance:
	print('Mean of ' + str(item) + ' in female data:' , round(df_female.loc[:,item].mean(),2))
for item in list_importance:
	print('Mean of ' + str(item) + ' in male data:' , round(df_male.loc[:,item].mean(),2))

for item in list_pref_o:
	print('Mean of ' + str(item) + ' in female data:' , round(df_female.loc[:,item].mean(),2))
	bar1.append(round(df_female.loc[:,item].mean(),2))
for item in list_pref_o:
	print('Mean of ' + str(item) + ' in male data:' , round(df_male.loc[:,item].mean(),2))
	bar2.append(round(df_male.loc[:,item].mean(),2))



barWidth = 0.25
 
=
r1 = np.arange(len(bar1))
r2 = [x + barWidth for x in r1]
plt.figure(figsize=(10,5))
# Make the plot
plt.bar(r1, bar1, color='#7f6d5f', width=barWidth, edgecolor='white', label='female')
plt.bar(r2, bar2, color='#557f2d', width=barWidth, edgecolor='white', label='male')

 
plt.xlabel('Attributes')
plt.xticks([r + barWidth for r in range(len(bar1))], 
	['attractive', 'sincere', 'intelligence', 'funny', 'ambitious','interests'])
plt.title('Mean values of six attributes comparing female and male')
plt.legend()


plt.savefig('../assignment2_solution/barplot.png')


