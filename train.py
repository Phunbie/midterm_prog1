
import pandas as pd
import pickle
url = 'training_sample.csv'

df = pd.read_csv(url)


df.drop('UserID', axis=1,inplace=True)

"""Creating input(X) and target(y) column"""

X=df.drop('ordered',axis=1)
y=df.ordered


from imblearn.under_sampling import RandomUnderSampler

under = RandomUnderSampler(random_state=42)

X_und, y_und = under.fit_resample(X, y)



"""Splitting the dataset into train,test and validation"""

from sklearn.model_selection import train_test_split

X_train_full, X_test, y_train_full, y_test = train_test_split(X_und, y_und , test_size=0.2, random_state=1)

X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=0.25, random_state=1)


from sklearn.linear_model import LogisticRegression


fi_model= LogisticRegression(C= 1.0, penalty= 'l1', random_state = 1, solver = 'saga')
fi_model.fit(X_train_full, y_train_full)

output_file = 'model_logistic.bin'
output_file

with open(output_file,'wb') as f_out:
  pickle.dump(fi_model,f_out)

def predict(df, model):
    cat = pd.DataFrame([df])
    
    X = cat[col].values

    y_pred = model.predict_proba(X)[:, 1]

    return y_pred







