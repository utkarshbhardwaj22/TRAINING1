"""
    FEATURE EXTRACTION -> Count vectorizer

"""

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

print(vectorizer)

chat_log = [
    'Hello, How can i help you',
    'Hi, i need to raise complaint',
    'for which',
    'this is for my laptop'
]

print(chat_log)

X = vectorizer.fit_transform(chat_log)
print(X)