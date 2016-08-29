import pandas as pd



textdata = pd.read_csv("questionbank.txt",sep="\t")
textdata.Entity = textdata.Entity.str.strip()
textdata.Property = textdata.Property.str.strip()

### Make features
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,2),lowercase=True,norm = None)

tfidf = tfidf_vectorizer.fit_transform(textdata['Question'])

tf_vectorizer = CountVectorizer(ngram_range=(1,2),lowercase=True)
tf = tf_vectorizer.fit_transform(textdata['Question'])

X=tf


from sklearn.metrics import classification_report
import numpy as np
#Make predictors

from sklearn.ensemble import GradientBoostingClassifier
gbc_entity = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0)
gbc_entity.fit(X,textdata['Entity'])

gbc_property = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0)
gbc_property.fit(X,textdata['Property'])


#y_pred = gbc.predict(X.toarray())
#print classification_report(y,y_pred)

"""
from sknn.mlp import Classifier, Layer
layers=[Layer("Rectifier", units=100),Layer("Softmax")]
nn = Classifier(layers=layers,learning_rate=0.02,n_iter=10)
nn.fit(X, y)
y_pred = nn.predict(X.toarray())
print classification_report(y,y_pred)
"""


entity_dictionary={}
property_dictionary={}

for entity in textdata.Entity.unique():
	entity_dictionary[entity]= textdata.Property[textdata.Entity==entity].unique().tolist()

for property in textdata.Property.unique():
	property_dictionary[property]= textdata.Entity[textdata.Property==property].unique().tolist()

def predict_question(question):
	prediction = {}
	vector = tf_vectorizer.transform([question]).todense()
	entity_predictions = gbc_entity.predict_proba(vector)[0]
	property_predictions = gbc_property.predict_proba(vector)[0]

	
	prediction['entity_guess'],prediction['entity_prob'] = gbc_entity.classes_[np.argmax(entity_predictions)],entity_predictions.max()
	prediction['property_guess'],prediction['property_prob'] = gbc_property.classes_[np.argmax(property_predictions)],property_predictions.max()
	
	#make sure confidence is above a certain threshold
	if prediction['entity_prob'] > .75 or prediction['property_prob'] > .75:
		
		# look the highest probability prediction and make sure that the entity is consitent with the property
		if prediction['entity_prob']> prediction['property_prob'] :

			for i in property_predictions.argsort()[::-1]:
				if gbc_property.classes_[i] in entity_dictionary[prediction['entity_guess']]:
					prediction['property_guess'] = gbc_property.classes_[i]
					prediction['property_prob'] = property_predictions[i]
					break

		if prediction['property_prob']> prediction['entity_prob'] :
			for i in entity_predictions.argsort()[::-1]:
				
				if gbc_entity.classes_[i] in property_dictionary[prediction['property_guess']]:
					prediction['entity_guess'] = gbc_entity.classes_[i]
					prediction['entity_prob'] = entity_predictions[i]
					break
		print (prediction['entity_guess'],prediction['entity_prob'])
		print (prediction['property_guess'],prediction['property_prob'])
		return "I believe that you are asking about the %s of the %s" %(prediction['property_guess'],prediction['entity_guess'])
	else:
		print (prediction['entity_guess'],prediction['entity_prob'])
		print (prediction['property_guess'],prediction['property_prob'])
		return "I'm not sure I understand. Can you rephrase your question?"
	