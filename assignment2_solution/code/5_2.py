import pandas as pd
import matplotlib.pyplot as plt
INPUT_FILE = '../assg2_release/dating.csv'
df = pd.read_csv(INPUT_FILE)
dict_df_bins = {}
train_bins = {}
test_bins = {}
allFeatures = df.columns.values[2:-1]
decisions = df['decision'].unique()
train_accuracies = []
test_accuracies = []
def predict(data,summaries):
	probabilities = []	
	result = [0]*len(data)
	for i in range(len(data)):
		probabilities.append([])
		for decision_value in decisions:
			probability = 1
			for feature in allFeatures:

				record = data.loc[i,feature]
				if record in summaries[decision_value][feature].keys():
					probability *= summaries[decision_value][feature][record]
				
			probabilities[i].append(probability)
	for i in range(len(probabilities)):
		if probabilities[i][0]>probabilities[i][1]:
			result[i] = 1
	return result
			
def calculate_accuracy(prediction, label):
	count = 0
	for i in range(len(prediction)):
		if prediction[i] == label[i]:
			count+=1
	return round(float(count)/len(prediction),2)

def NBC(t_frac):
	df_frac= train_data.sample(frac=t_frac,random_state=47) 
	summaries = {}
	for decision_value in decisions:
		summaries[decision_value] = {}
		for feature in allFeatures:
			summaries[decision_value][feature] ={}
			for feature_value in df_frac[feature].unique():
				summaries[decision_value][feature][feature_value] = float(len(df_frac[(df_frac['decision']==decision_value)&(df_frac[feature]==feature_value)]))/len(df_frac[df_frac['decision']==decision_value])
	train_prediction = predict(train_data, summaries)
	test_prediction = predict(test_data,summaries)
	train_accuracy = calculate_accuracy(train_prediction, train_data['decision'])
	test_accuracy = calculate_accuracy(test_prediction,test_data['decision'])
	train_accuracies.append(train_accuracy)
	test_accuracies.append(test_accuracy)
	print('Training accuracy: ', train_accuracy)
	print('Testing accuracy: ', test_accuracy)

variables = df.drop(columns = ["Unnamed: 0", "gender", "race", "race_o", "samerace", "field", "decision"])
continuous_variables = variables.columns.values
bin_sizes = [2,5,10,50,100,200]

def discretize_and_split(bin_size):
	df_binned = pd.read_csv(INPUT_FILE)
	for item in continuous_variables:
		df_binned[item] = pd.cut(df_binned[item],bin_size)

	test_data = df_binned.sample(frac=0.2,random_state=47) 
	train_data = df_binned.drop(test_data.index)
	return train_data, test_data

for bin_size in bin_sizes:
	train_data, test_data = discretize_and_split(bin_size)
	train_data.reset_index(drop=True,inplace=True)
	test_data.reset_index(drop=True,inplace=True)
	print('bin size: ', bin_size)
	NBC(1)
positions = (2, 5, 10,50,100,200)
labels = (2, 5, 10,50,100,200)
plt.figure(figsize=(10,5))
plt.plot(bin_sizes,train_accuracies)
plt.plot(bin_sizes,test_accuracies)
plt.title('train vs test accuracy with different bin sizes ')
plt.xticks(positions,labels)
plt.xlabel('bin size')
plt.ylabel('accuracy')
plt.legend(['train accuracy', 'test accuracy'], loc = 'upper left')

plt.savefig('../assignment2_solution/accuracy_with_bins.png')