import pandas as pd

filepath = {'emorynlp_train_final.csv'}

df=pd.read_csv('docs\MELD-dataset\data\emorynlp\emorynlp_train_final.csv',usecols=['Utterance', 'Emotion'])
print(df)
