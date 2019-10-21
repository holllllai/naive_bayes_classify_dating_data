import pandas as pd
INPUT_FILE = '../assg2_release/dating-binned.csv'
df = pd.read_csv(INPUT_FILE)
test=df.sample(frac=0.2,random_state=47) 
train=df.drop(test.index)

train_out = '../assg2_release/trainingSet.csv'
test_out = '../assg2_release/testSet.csv'

train.to_csv(train_out)
test.to_csv(test_out)