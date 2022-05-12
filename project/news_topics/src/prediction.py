from preprocessing import preprocess as prep
import pickle
import os

path = os.getcwd()

with open(os.path.join(path, "data/topics.pkl"), "rb") as file:
  topics = pickle.load(file)

with open(os.path.join(path, "models/tv.pkl"), "rb") as file:
  tv = pickle.load(file)

with open(os.path.join(path, "models/svm.pkl"), "rb") as file:
  svm = pickle.load(file)

def svm_predict(text):
    token = prep(text)
    
    X = tv.transform([token]).toarray()
    result = svm.predict(X)

    return topics[result[0]]