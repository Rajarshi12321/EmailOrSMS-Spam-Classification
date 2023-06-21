import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
import streamlit as st
import pickle
import sklearn

tfdif = pickle.load(open("Vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

st.title("Email and SMS Classifier")

input_sms = st.text_area("Enter the message")

ps = PorterStemmer()


def transform(input):
    # Changing to lowercase
    input = input.lower()

    # Tokenizing Words
    input = nltk.word_tokenize(input)

    # Removal of Special Characters
    list = []
    for i in input:
        if i.isalnum():
            list.append(i)

    # Removal of punctuations
    input = list[:]
    list.clear()

    for i in input:
        if i not in stopwords.words("english") and i not in string.punctuation:
            list.append(i)

    # Stemming
    input = list[:]
    list.clear()

    for i in input:
        list.append(ps.stem(i))

    return " ".join(list)


if st.button("Predict"):
    # 1. Preprocessing

    transform_sms = transform(input_sms)

    # 2. Vectorize

    vector_input = tfdif.transform([transform_sms])

    # 3. Predict

    result = model.predict(vector_input)[0]

    # 4. Display

    if result == 1:
        st.header("The above message is a Spam")

    else:
        st.header("The above message is not a Spam")
