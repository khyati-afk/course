import streamlit as st

if "history" not in st.session_state:
    st.session_state.history = []

knowledge = {
    "how are you": "I'm fine. How are you?",
    "i feel sad": "I'm sorry to hear that. What's bothering you?",
    "i am lonely": "Feeling lonely can be tough.",
    "i'm stressed": "What's been stressing you out?",
    "i feel lost": "It's okay to feel lost sometimes.",
    "i need someone to talk to": "Tell me what's on your mind, and I'll listen.",
    "i feel worthless": "Can you share more about what's making you feel this way?",
    "i can't sleep": "Have you tried deep breathing or listening to soothing music before bed?",
    "i feel hopeless": "Would you like to talk about what's causing these feelings?",
    "i feel angry": "Anger can be intense. Do you want to talk about what's making you angry?",
    "i need motivation": "Starting small and celebrating small wins can make a big difference.",
    "i feel empty": "Sometimes, connecting with loved ones or engaging in hobbies can help.",
    "i'm nervous": "Try focusing on your breathing or thinking about something that makes you happy.",
    "i don't know what to do": "Let's break it down together. What's been on your mind?",
    "default":"Sorry I didn't get you"
}

weights = {'how':1, 'are':1, 'you':1, 'i':1, 'feel':2, 'sad':5, 'am':1, 'lonely':5, "i'm":1, 'stressed':5, 'lost':5,
           'need':3, 'someone':2, 'to':1, 'talk':2, 'worthless':4, "can't":2, 'sleep':4, 'hopeless':5, 'angry':5,
           'motivation':4, 'empty':4, 'nervous':4, "don't":2, 'know':3, 'what':1, 'do':1, 'default':7}

def weighted_manhattan_distance(doc1, doc2): # these docs should be lists of words
    vocab = []
    for word in doc1:
        if word not in vocab:
            vocab.append(word)
    for word in doc2:
        if word not in vocab:
            vocab.append(word)
    vec1 = []
    vec2 = []
    for word in vocab:
        vec1.append(doc1.count(word))
        vec2.append(doc2.count(word))
    distance = 0
    for i, word in enumerate(vocab):
        wt = 1
        if word in weights:
            wt = weights[word]
        distance += abs(vec1[i] - vec2[i]) * wt
    return distance

st.title("Chatbot")

st.write("Hello, how can I help you?")
req = st.text_input("Your message: ").lower()
query = req.split()

closest_key = "default"
closest_dist = 10

if query:
    for key in knowledge:
        dist = weighted_manhattan_distance(query, key.split())
        if dist < closest_dist:
            closest_dist = dist
            closest_key = key
    res = knowledge[closest_key]
    pair = {'req':req, 'res':res}
    st.session_state.history.append(pair)

for pair in st.session_state.history:
    st.info(pair['req'])
    st.write(pair['res'])