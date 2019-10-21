import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

INPUT_FILE = '../assg2_release/dating.csv'
df = pd.read_csv(INPUT_FILE)

df['age'] = pd.cut(df['age'],5)
age_bin_count = []
for i in range(5):
	age_bin_count.append(df['age'].value_counts()[i])
print('age: ',age_bin_count)

df['age_o'] = pd.cut(df['age_o'],5)
ageo_bin_count = []
for i in range(5):
	ageo_bin_count.append(df['age_o'].value_counts()[i])
print('age_0: ',ageo_bin_count)

df['importance_same_race'] = pd.cut(df['importance_same_race'],5)
isr_bin_count = []
for i in range(5):
	isr_bin_count.append(df['importance_same_race'].value_counts()[i])
print('importance_same_race: ',isr_bin_count)

df['importance_same_religion'] = pd.cut(df['importance_same_religion'],5)
isre_bin_count = []
for i in range(5):
	isre_bin_count.append(df['importance_same_religion'].value_counts()[i])
print('importance_same_religion: ',isre_bin_count)

df['pref_o_attractive'] = pd.cut(df['pref_o_attractive'],5)
pratt_bin_count = []
for i in range(5):
	pratt_bin_count.append(df['pref_o_attractive'].value_counts()[i])
print('pref_o_attractive: ',pratt_bin_count)

df['pref_o_sincere'] = pd.cut(df['pref_o_sincere'],5)
posin_bin_count = []
for i in range(5):
	posin_bin_count.append(df['pref_o_sincere'].value_counts()[i])
print('pref_o_sincere: ',posin_bin_count)

df['pref_o_intelligence'] = pd.cut(df['pref_o_intelligence'],5)
pref_o_intelligence_bin_count = []
for i in range(5):
	pref_o_intelligence_bin_count.append(df['pref_o_intelligence'].value_counts()[i])
print('pref_o_intelligence: ',pref_o_intelligence_bin_count)

df['pref_o_funny'] = pd.cut(df['pref_o_funny'],5)
pref_o_funny_bin_count = []
for i in range(5):
	pref_o_funny_bin_count.append(df['pref_o_funny'].value_counts()[i])
print('pref_o_funny: ',pref_o_funny_bin_count)

df['pref_o_ambitious'] = pd.cut(df['pref_o_ambitious'],5)
pref_o_ambitious_bin_count = []
for i in range(5):
	pref_o_ambitious_bin_count.append(df['pref_o_ambitious'].value_counts()[i])
print('pref_o_ambitious: ',pref_o_ambitious_bin_count)

df['pref_o_shared_interests'] = pd.cut(df['pref_o_shared_interests'],5)
pref_o_shared_interests_bin_count = []
for i in range(5):
	pref_o_shared_interests_bin_count.append(df['pref_o_shared_interests'].value_counts()[i])
print('pref_o_shared_interests: ',pref_o_shared_interests_bin_count)


df['attractive_important'] = pd.cut(df['attractive_important'],5)
attractive_important_bin_count = []
for i in range(5):
	attractive_important_bin_count.append(df['attractive_important'].value_counts()[i])
print('attractive_important: ',attractive_important_bin_count)

df['sincere_important'] = pd.cut(df['sincere_important'],5)
sincere_important_bin_count = []
for i in range(5):
	sincere_important_bin_count.append(df['sincere_important'].value_counts()[i])
print('sincere_important: ',sincere_important_bin_count)

df['intelligence_important'] = pd.cut(df['intelligence_important'],5)
intelligence_important_bin_count = []
for i in range(5):
	intelligence_important_bin_count.append(df['intelligence_important'].value_counts()[i])
print('intelligence_important: ',intelligence_important_bin_count)

df['funny_important'] = pd.cut(df['funny_important'],5)
funny_important_bin_count = []
for i in range(5):
	funny_important_bin_count.append(df['funny_important'].value_counts()[i])
print('funny_important: ',funny_important_bin_count)

df['ambition_important'] = pd.cut(df['ambition_important'],5)
ambition_important_bin_count = []
for i in range(5):
	ambition_important_bin_count.append(df['ambition_important'].value_counts()[i])
print('ambition_important: ',ambition_important_bin_count)

df['shared_interests_important'] = pd.cut(df['shared_interests_important'],5)
shared_interests_important_bin_count = []
for i in range(5):
	shared_interests_important_bin_count.append(df['shared_interests_important'].value_counts()[i])
print('shared_interests_important: ',shared_interests_important_bin_count)

df['attractive'] = pd.cut(df['attractive'],5)
attractive_bin_count = []
for i in range(5):
	attractive_bin_count.append(df['attractive'].value_counts()[i])
print('attractive: ',attractive_bin_count)

df['sincere'] = pd.cut(df['sincere'],5)
sincere_bin_count = []
for i in range(5):
	sincere_bin_count.append(df['sincere'].value_counts()[i])
print('sincere: ',sincere_bin_count)

df['intelligence'] = pd.cut(df['intelligence'],5)
intelligence_bin_count = []
for i in range(5):
	intelligence_bin_count.append(df['intelligence'].value_counts()[i])
print('intelligence: ',intelligence_bin_count)

df['funny'] = pd.cut(df['funny'],5)
funny_bin_count = []
for i in range(5):
	funny_bin_count.append(df['funny'].value_counts()[i])
print('funny: ',funny_bin_count)

df['ambition'] = pd.cut(df['ambition'],5)
ambition_bin_count = []
for i in range(5):
	ambition_bin_count.append(df['ambition'].value_counts()[i])
print('ambition: ',ambition_bin_count)

df['attractive_partner'] = pd.cut(df['attractive_partner'],5)
attractive_partner_bin_count = []
for i in range(5):
	attractive_partner_bin_count.append(df['attractive_partner'].value_counts()[i])
print('attractive_partner: ',attractive_partner_bin_count)

df['sincere_partner'] = pd.cut(df['sincere_partner'],5)
sincere_partner_bin_count = []
for i in range(5):
	sincere_partner_bin_count.append(df['sincere_partner'].value_counts()[i])
print('sincere_partner: ',sincere_partner_bin_count)


df['intelligence_parter'] = pd.cut(df['intelligence_parter'],5)
intelligence_partner_bin_count = []
for i in range(5):
	intelligence_partner_bin_count.append(df['intelligence_parter'].value_counts()[i])
print('intelligence_parter: ',intelligence_partner_bin_count)

df['funny_partner'] = pd.cut(df['funny_partner'],5)
funny_partner_bin_count = []
for i in range(5):
	funny_partner_bin_count.append(df['funny_partner'].value_counts()[i])
print('funny_partner: ',funny_partner_bin_count)

df['ambition_partner'] = pd.cut(df['ambition_partner'],5)
ambition_parter_bin_count = []
for i in range(5):
	ambition_parter_bin_count.append(df['ambition_partner'].value_counts()[i])
print('ambition_partner: ',ambition_parter_bin_count)


df['shared_interests_partner'] = pd.cut(df['shared_interests_partner'],5)
shared_interests_partner_bin_count = []
for i in range(5):
	shared_interests_partner_bin_count.append(df['shared_interests_partner'].value_counts()[i])
print('shared_interests_partner: ',ambition_parter_bin_count)

df['sports'] = pd.cut(df['sports'],5)
sports_bin_count = []
for i in range(5):
	sports_bin_count.append(df['sports'].value_counts()[i])
print('sports: ',sports_bin_count)

df['tvsports'] = pd.cut(df['tvsports'],5)
tvsports_bin_count = []
for i in range(5):
	tvsports_bin_count.append(df['tvsports'].value_counts()[i])
print('tvsports: ',tvsports_bin_count)

df['exercise'] = pd.cut(df['exercise'],5)
exercise_bin_count = []
for i in range(5):
	exercise_bin_count.append(df['exercise'].value_counts()[i])
print('exercise: ',exercise_bin_count)

df['dining'] = pd.cut(df['dining'],5)
dining_bin_count = []
for i in range(5):
	dining_bin_count.append(df['dining'].value_counts()[i])
print('dining: ',dining_bin_count)

df['museums'] = pd.cut(df['museums'],5)
museums_bin_count = []
for i in range(5):
	museums_bin_count.append(df['museums'].value_counts()[i])
print('museums: ',museums_bin_count)

df['art'] = pd.cut(df['art'],5)
art_bin_count = []
for i in range(5):
	art_bin_count.append(df['art'].value_counts()[i])
print('art: ',art_bin_count)

df['hiking'] = pd.cut(df['hiking'],5)
hiking_bin_count = []
for i in range(5):
	hiking_bin_count.append(df['hiking'].value_counts()[i])
print('hiking: ',hiking_bin_count)

df['gaming'] = pd.cut(df['gaming'],5)
gaming_bin_count = []
for i in range(5):
	gaming_bin_count.append(df['gaming'].value_counts()[i])
print('gaming: ',gaming_bin_count)

df['clubbing'] = pd.cut(df['clubbing'],5)
clubbing_bin_count = []
for i in range(5):
	clubbing_bin_count.append(df['clubbing'].value_counts()[i])
print('clubbing: ',clubbing_bin_count)

df['reading'] = pd.cut(df['reading'],5)
reading_bin_count = []
for i in range(5):
	reading_bin_count.append(df['reading'].value_counts()[i])
print('reading: ',reading_bin_count)

df['tv'] = pd.cut(df['tv'],5)
tv_bin_count = []
for i in range(5):
	tv_bin_count.append(df['tv'].value_counts()[i])
print('tv: ',tv_bin_count)

df['theater'] = pd.cut(df['theater'],5)
theater_bin_count = []
for i in range(5):
	theater_bin_count.append(df['theater'].value_counts()[i])
print('theater: ',theater_bin_count)

df['movies'] = pd.cut(df['movies'],5)
movies_bin_count = []
for i in range(5):
	movies_bin_count.append(df['movies'].value_counts()[i])
print('movies: ',movies_bin_count)

df['concerts'] = pd.cut(df['concerts'],5)
concerts_bin_count = []
for i in range(5):
	concerts_bin_count.append(df['concerts'].value_counts()[i])
print('concerts: ',concerts_bin_count)

df['music'] = pd.cut(df['music'],5)
music_bin_count = []
for i in range(5):
	music_bin_count.append(df['music'].value_counts()[i])
print('music: ',music_bin_count)

df['shopping'] = pd.cut(df['shopping'],5)
shopping_bin_count = []
for i in range(5):
	shopping_bin_count.append(df['shopping'].value_counts()[i])
print('shopping: ',shopping_bin_count)

df['yoga'] = pd.cut(df['yoga'],5)
yoga_bin_count = []
for i in range(5):
	yoga_bin_count.append(df['yoga'].value_counts()[i])
print('yoga: ',yoga_bin_count)

df['interests_correlate'] = pd.cut(df['interests_correlate'],5)
interests_correlate_bin_count = []
for i in range(5):
	interests_correlate_bin_count.append(df['interests_correlate'].value_counts()[i])
print('interests_correlate: ',interests_correlate_bin_count)

df['expected_happy_with_sd_people'] = pd.cut(df['expected_happy_with_sd_people'],5)
expected_happy_with_sd_people_bin_count = []
for i in range(5):
	expected_happy_with_sd_people_bin_count.append(df['expected_happy_with_sd_people'].value_counts()[i])
print('expected_happy_with_sd_people: ',expected_happy_with_sd_people_bin_count)

df['like'] = pd.cut(df['like'],5)
like_bin_count = []
for i in range(5):
	like_bin_count.append(df['like'].value_counts()[i])
print('like: ',like_bin_count)

OUTPUT_FILE = '../assg2_release/dating-binned.csv'

df.to_csv(OUTPUT_FILE)







