# A free and opensource framework to build and share (ML & DS) web apps

# !pip install streamlit
# !python -m streamlit run main.py

import streamlit as st

# Headings
st.title("This is a Title")  # Largest heading
st.header("This is a Header")  # Secondary heading
st.subheader("This is a Subheader")  # Tertiary heading
# Plain Texts
st.text("st.text: Some text") # to display plain text
st.write("st.write: Some text") # more versatile than text, can handle (dataframes, markdowns, etc.)

st.text("**Khyati**")
st.write("**Khyati**")

# Formatted Texts
st.caption("st.caption: This is a caption.")
st.markdown("st.markdown: **Bold text**, *italic text*, and click on the [link](https://www.google.com).")
st.latex(r"st.latex: a^2 + b^2 = c^2")
# Coding Texts
st.code("""
def hello_world():
    print("Hello, World!")
""", language="python")

# Special Messages
st.success("This is a success message!")
st.error("This is an error message.")
st.warning("This is a warning.")
st.info("This is an informational message.")

data = {"count": 3, "students": [{"Alice":11, "Bob":12, "Charlie":13}]}
st.json(data)

# Expander
with st.expander("Expand for more details"):
    st.write("Here is some detailed information.")

# Button
if st.button("Click Me"):
    st.write("Button clicked!")
else:
    st.write("Click the button to see something happen.")

# Text area
text = st.text_area("Enter a long message")
st.text(f"You wrote: {text}")

# Text input
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")

# Number input
age = st.number_input("Enter your age", min_value=0, max_value=120, value=20)
if age:
    st.write(f"You are {age} years old.")

# Slider
value = st.slider("Select a value", min_value=0, max_value=100, value=50)
st.write(f"Selected value: {value}")

# Select slider
level = st.select_slider("Choose a level", options=["Low", "Medium", "High"], value="Medium")
st.write(f"You selected: {level}")

# Checkbox
check = st.checkbox("Show Text")
st.write(check)
if check:
    st.write("You checked the box!")

# Radio
choice = st.radio("Pick one:", ["A", "B", "C"])
st.write(f"You chose: {choice}")

# Selectbox
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

# CheckGroup
selected = []
option1 = st.checkbox("Option 1")
if option1:
    selected.append("Option 1")
option2 = st.checkbox("Option 2")
if option2:
    selected.append("Option 2")
option3 = st.checkbox("Option 3")
if option3:
    selected.append("Option 3")
st.write(f"You selected: {selected}")

# Multiselect
options = st.multiselect("Choose multiple options", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {options}")

# Date
date = st.date_input("Pick a date")
st.write(f"Selected date: {date}")

# Form
with st.form("my_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0)
    submitted = st.form_submit_button("Submit")
if submitted:
    st.write("Form submitted!")
    st.write(f"Hello {name}, you are {age} years old!")

# File uploader
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt", "xlsx"])
if uploaded_file is not None:
    st.write("Uploaded file name:", uploaded_file.name)

# Color picker
color = st.color_picker("Pick a color", "#00f900")
st.write(f"The selected color is {color}")

# Progress bar
import time
st.subheader("Progress Bar")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    progress.progress(i + 1)
st.write("Task completed!")

# Spinner
st.subheader("Spinner")
with st.spinner('Loading...'):
    for i in range(100):
        time.sleep(0.05)
        progress.progress(i + 1)
st.write("Task completed!")