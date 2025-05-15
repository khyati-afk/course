# !pip install streamlit
# !python -m streamlit run main.py

import streamlit as st
from PIL import Image

### IMAGES ###

# Load image from URL
st.header("Image from URL")
img_url = "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-lighttext.png"
st.image(img_url, caption="Image from URL")

# Load image from file
st.header("Image from file")
img = Image.open(".//assets//image.png")
st.image(img, caption="My Uploaded Image")

### AUDIOS ###

# Load audio from URL
st.header("Audio from URL")
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url)

# Load audio from file
st.header("Audio from file")
audio_file = open(".//assets//audio.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mpeg")

### VIDEOS ###

# Load video from URL
st.header("Video from URL")
video_url = "https://youtu.be/dQw4w9WgXcQ?si=twGniNRaP866vwoA"
if st.button("Click to play video"):
    st.video(video_url)

# Load video from file
st.header("Video from file")
video_file = open(".//assets//video.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

### TABLES ###
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 22],
    "Marks1": [67, 78, 89],
    "Marks2": [67, 78, 89],
    "Marks3": [67, 78, 89],
    "Marks4": [67, 78, 89],
    "Marks5": [67, 78, 89],
    "Marks6": [67, 78, 89],
    "Marks7": [67, 78, 89],
    "Marks8": [67, 78, 89],
    "Marks9": [67, 78, 89],
    "Marks10": [67, 78, 89],
    "Marks11": [67, 78, 89],
    "Marks12": [67, 78, 89],
}
# df = pd.DataFrame(data)
df = pd.read_csv(".//assets//data.csv")

# Static table (no scroll/sort)
st.header("Static Table (using st.table)")
st.table(df)

# Interactive table (sortable & scrollable)
st.header("Interactive Table (using st.dataframe)")
st.dataframe(df)

st.header("Interactive Table (using st.write)")
st.write(df)
