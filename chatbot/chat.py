import random
import json

import torch
from chatbot.model import NeuralNet
from chatbot.nltk_utils import bag_of_words, tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from spellchecker import SpellChecker

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('chatbot/dataset/intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "chatbot/dataset/data.pth"
data = torch.load(FILE)

model_state = data["model_state"]
input_size = data["input_size"]
output_size = data["output_size"]
hidden_size = data["hidden_size"]
all_words = data['all_words']
tags = data['tags']

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

# Initialize spell checker and lemmatizer
spell = SpellChecker()
lemmatizer = WordNetLemmatizer()

def correct_spelling(user_input):
    corrected_words = []
    for word in user_input.split():
        correction = spell.correction(word)
        if correction:
            corrected_words.append(correction)
        else:
            corrected_words.append(word)  # Use original word if no correction found
    return ' '.join(corrected_words)


def preprocess_input(user_input):
    user_input_corrected = correct_spelling(user_input.lower())
    user_input_lemmatized = ' '.join([lemmatizer.lemmatize(word) for word in user_input_corrected.split()])
    return user_input_lemmatized

def predict_intent(user_input):
    user_input_processed = preprocess_input(user_input)
    user_vector = CountVectorizer.transform([user_input_processed])
    similarities = cosine_similarity(user_vector, X).flatten()
    if similarities.max() == 0:
        return None
    idx = similarities.argmax()
    return tags[idx]

def get_Response(sentence):
    sentence = preprocess_input(sentence)  # Preprocess input sentence
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
            
    return "I do not understand"

if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_Response(sentence)
        print(resp)
