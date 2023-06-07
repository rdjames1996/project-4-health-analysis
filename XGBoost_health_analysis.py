#!/usr/bin/env python
# coding: utf-8

# ## Preprocessing

# In[1]:


# Import our dependencies
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import pandas as pd
import tensorflow as tf


#  Import and read the charity_data.csv.
import pandas as pd 
diabetes_df = pd.read_csv(r"C:\Users\Louie\OneDrive\Desktop\uci\project-4-health-analysis\Ana\diabetes_binary_5050split_health_indicators_BRFSS2015.csv")
diabetes_df.head()

print(diabetes_df.columns)
# In[2]:


diabetes_binary_df_clean = diabetes_df.drop(columns=['NoDocbcCost ', 'GenHlth ', 'MentHlth ', 'PhysHlth ', 'DiffWalk ', 'CholCheck '])
diabetes_binary_df_clean = diabetes_binary_df_clean.rename(columns={'Diabetes_binary ': 'Diabetes_binary', 'HighBP ': 'HighBP', 'HighChol ' : 'HighChol',
                                                                    'BMI  ' : 'BMI', 'Smoker ' : 'Smoker', 'Stroke ' : 'Stroke', 'HeartDiseaseorAttack ' :'HeartDiseaseorAttack',
                                                                    'PhysActivity ' : 'PhysActivity', 'Fruits ' : 'Fruits', 'Veggies ' : 'Veggies', 'HvyAlcoholConsump ' : 'HvyAlcoholConsump',
                                                                    'AnyHealthcare ' : 'AnyHealthcare', 'Sex ' : 'Sex', 'Age  ' : 'Age', 'Education ' : 'Education'
                                                                    })
diabetes_binary_df_clean

# In[20]:


diabetes_binary_df_clean.columns.to_list()


# In[3]:


#Randomize Data
diabetes_df_random = diabetes_binary_df_clean.sample(frac=1)


# In[4]:


# Split our preprocessed data into our features and target arrays
y = diabetes_df_random['Diabetes_binary'].values
X = diabetes_df_random.drop(columns='Diabetes_binary').values

# Split the preprocessed data into a training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# In[5]:


from sklearn.pipeline import Pipeline
#from category_encoders.target_encoder import TargetEncoder
from xgboost import XGBClassifier

estimators = [
    #('encoder', TargetEncoder()),
    ('clf', XGBClassifier(random_state=1))
]
pipe = Pipeline(steps=estimators)
pipe


# In[7]:


from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer

search_space = {
    'clf__max_depth': Integer(2,8),
    'clf__learning_rate': Real(0.001, 1.0, prior='log-uniform'),
    'clf__subsample': Real(0.5,1.0),
    'clf__colsample_bytree': Real(0.5,1.0),
    'clf__colsample_bylevel': Real(0.5,1.0),
    'clf__colsample_bynode': Real(0.5,1.0),
    'clf__reg_alpha': Real(0.0,10.0),
    'clf__reg_lambda': Real(0.0,10.0),
    'clf__gamma': Real(0.0, 10.0)
}

opt = BayesSearchCV(pipe, search_space, cv=3, n_iter=10, scoring= 'roc_auc', random_state=1)


# In[8]:


#Train XGBoost model
opt.fit(X_train, y_train)


# In[9]:


#Evaluate the model and make predictions
opt.predict_proba(X_test)


# In[10]:


opt.best_estimator_


# In[11]:


opt.best_score_


# In[12]:


opt.score(X_test, y_test)


# In[13]:


opt.predict(X_test)


# In[14]:


opt.best_estimator_.steps


# In[15]:


from xgboost import plot_importance
xgboost_step = opt.best_estimator_.steps[0]
xgboost_model = xgboost_step[1]
plot_importance(xgboost_model)


# In[16]:


clf_pickle = xgboost_model
clf_pickle


# In[17]:


import pickle
pickle.dump(clf_pickle, open('model.pkl', 'wb'))


# In[18]:


with open('model.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)


# In[ ]:




