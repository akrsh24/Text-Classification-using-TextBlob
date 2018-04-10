
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv(r'C:\Users\akasriva2\Downloads\Consumer_Complaints.csv')
df.head()


# In[2]:


df = df[pd.notnull(df['Consumer complaint narrative'])]


# In[3]:


df.info()


# In[4]:


col = ['Product', 'Consumer complaint narrative']
df = df[col]


# In[5]:


df.columns


# In[6]:


df.columns = ['Product', 'Consumer_complaint_narrative']


# In[7]:


df['category_id'] = df['Product'].factorize()[0]
from io import StringIO
category_id_df = df[['Product', 'category_id']
                    ].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Product']].values)


# In[8]:


df.head()


# In[9]:


import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 6))
df.groupby('Product').Consumer_complaint_narrative.count().plot.bar(ylim=0)
plt.show()


# In[10]:


from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2',
                        encoding='latin-1', ngram_range=(1, 2), stop_words='english')

features = tfidf.fit_transform(df.Consumer_complaint_narrative).toarray()
labels = df.category_id
features.shape


# In[11]:


from sklearn.feature_selection import chi2
import numpy as np

N = 2
for Product, category_id in sorted(category_to_id.items()):
    features_chi2 = chi2(features, labels == category_id)
    indices = np.argsort(features_chi2[0])
    feature_names = np.array(tfidf.get_feature_names())[indices]
    unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
    bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
    print("# '{}':".format(Product))
    print("  . Most correlated unigrams:\n       . {}".format(
        '\n       . '.join(unigrams[-N:])))
    print("  . Most correlated bigrams:\n       . {}".format(
        '\n       . '.join(bigrams[-N:])))


# In[12]:


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

X_train, X_test, y_train, y_test = train_test_split(
    df['Consumer_complaint_narrative'], df['Product'], random_state=0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_tfidf, y_train)


# In[13]:


print(clf.predict(count_vect.transform(
    ["This company refuses to provide me verification and validation of debt per my right under the FDCPA. I do not believe this debt is mine."])))


# In[14]:


df[df['Consumer_complaint_narrative'] ==
    "This company refuses to provide me verification and validation of debt per my right under the FDCPA. I do not believe this debt is mine."]


# In[15]:


from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

from sklearn.model_selection import cross_val_score


models = [
    RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
    LinearSVC(),
    MultinomialNB(),
    LogisticRegression(random_state=0),
]
CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = []
for model in models:
    model_name = model.__class__.__name__
    accuracies = cross_val_score(
        model, features, labels, scoring='accuracy', cv=CV)
    for fold_idx, accuracy in enumerate(accuracies):
        entries.append((model_name, fold_idx, accuracy))
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])


# In[16]:


import seaborn as sns

sns.boxplot(x='model_name', y='accuracy', data=cv_df)
sns.stripplot(x='model_name', y='accuracy', data=cv_df,
              size=8, jitter=True, edgecolor="gray", linewidth=2)
plt.show()


# In[17]:


cv_df.groupby('model_name').accuracy.mean()

