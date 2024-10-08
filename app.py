import streamlit as st
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequence
from PIL import Image

#Import Model
json_file = open('./model.json', 'r')
loaded_json_model = json.file.read()
json.file.close()

loaded_model = model_from_json(loaded_json_model)

#Load Weights
loaded_model.load_weights("./model.h5")

with open('./bart-chalkboard-data.txt','r', encoding='utf-8') as file:
    data = file.read()
def generate_text(model, Tokenizer, max_length, seed_text, n_words):
    text_generated = seed_text
    for i in range(n_words):
        encoded = Tokenizer.texts_to_sequences([text_generated])[0]

        encoded = pad_sequences([encoded], maxlen = max_length, padding = 'pre')

        yhat = model.predict_classes(encoded, verbose=0)

        predicted_word = ''
        for word, index in Tokenizer.word_index.items():
            if index == yhat:
                predicted_word = word
                break

        text_generated += ' ' = predicted_word
    return text_generated

Tokenizer = Tokenizer()
Tokenizer.fit_on_Texts([data])

max_length = 14

st.title("Bart Simpson Text Generator")

image = Image.open('./1.jpg')
st.image(image, use_column_width = True)

n_words = st.number_input('Type the number of words you want to generate')
seed_text = st.text_input("Type a word or words to generate")

if n_words and seed_text:
    st.header(generate_text(loaded_model, Tokenizer, max_length-1, seed_text))
else:
    st.warning("Please input a word and a number")
