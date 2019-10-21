import pandas as pd
INPUT_FILE = '../assg2_release/dating-binned.csv'
df = pd.read_csv(INPUT_FILE)
train_data = pd.read_csv('../assg2_release/trainingSet.csv')
test_data = pd.read_csv('../assg2_release/testSet.csv')
allFeatures = df.columns.values[2:-1]
decisions = df['decision'].unique()
print(decisions)

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
	print('Training accuracy: ', train_accuracy)
	print('Testing accuracy: ', test_accuracy)
	

	
NBC(1)

