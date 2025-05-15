# To install streamlit   : !pip install streamlit
# To run a streamlit app : python -m streamlit run .\01_main.py
import streamlit as st

st.title("HOMEWORK")
st.header("Calculator")

x = st.text_input("Enter first number:")
y = st.text_input("Enter second number:")

operation = st.selectbox("Select operation", ["+", "-", "*", "/"])

if st.button("Calculate"):
    try:
        x = float(x)
        y = float(y)

        if operation == "+":
            result = x + y
        elif operation == "-":
            result = x - y
        elif operation == "*":
            result = x * y
        elif operation == "/":
            if y == 0:
                st.error("Error: Division by zero is not allowed.")
                result = None
            else:
                result = x / y

        if result is not None:
            st.success(f"Result: {result}")
    except ValueError:
        st.error("Please enter valid numbers.")


# ----------------------------------------------------------------------------------------------------------------

st.header("Create Your Portfolio")

name = st.text_input("Your Full Name")
age = st.number_input("Your Age", min_value=0, max_value=120, step=1)
about = st.text_area("About Me", height=100)

st.subheader("Skills")
skills = st.text_area("List your skills (separate by commas)", height=80)

st.subheader("Projects")
project1_name = st.text_input("Project 1 Name")
project1_link = st.text_input("Project 1 Link (URL)")
project1_desc = st.text_area("Project 1 Description", height=100)

project2_name = st.text_input("Project 2 Name")
project2_link = st.text_input("Project 2 Link (URL)")
project2_desc = st.text_area("Project 2 Description", height=100)

st.subheader("Contact Info")
email = st.text_input("Email address")

if name:
    st.markdown(f"## {name}")
    if age:
        st.markdown(f"**Age:** {int(age)}")

if about:
    st.markdown("### About Me")
    st.write(about)

if skills:
    st.markdown("### Skills")
    skill_list = [s.strip() for s in skills.split(",") if s.strip()]
    for skill in skill_list:
        st.write(f"- {skill}")

if email:
    st.markdown("### Contact")
    st.write(f"Email: {email}")

# ----------------------------------------------------------------------------------------------------------------
import streamlit as st

veg_pizzas = {"Margherita": 150, "Farmhouse": 180, "Peppy Paneer": 200}

non_veg_pizzas = {"Chicken Tikka": 220, "Pepperoni": 250, "Barbecue Chicken": 240}

topping_options = {
    "Onions": 20,
    "Capsicum": 25,
    "Mushrooms": 30,
    "Olives": 20,
    "Jalapenos": 15,
}

combo_items = {
    "Cola": 50,
    "Orange Juice": 60,
    "Fries": 100,
    "Garlic Bread": 120,
}

extra_cheese_price = 40

st.title("Pizza Order Form")

base_type = st.radio("Choose your pizza base:", ["Veg", "Non-Veg"])

if base_type == "Veg":
    pizza = st.selectbox("Select your pizza:", list(veg_pizzas.keys()))
    pizza_price = veg_pizzas[pizza]
else:
    pizza = st.selectbox("Select your pizza:", list(non_veg_pizzas.keys()))
    pizza_price = non_veg_pizzas[pizza]

extra_cheese = st.checkbox("Add extra cheese? (+₹40)")

chosen_toppings = st.multiselect(
    "Choose toppings (₹ per topping shown):",
    options=list(topping_options.keys()),
    help="Select one or more toppings",
)

toppings_price = sum(topping_options[t] for t in chosen_toppings)

chosen_combo = st.multiselect(
    "Add other items to your combo:", options=list(combo_items.keys())
)

combo_price = sum(combo_items[item] for item in chosen_combo)

total_price = pizza_price + toppings_price + combo_price
if extra_cheese:
    total_price += extra_cheese_price

toppings_text = (
    " with " + ", ".join(chosen_toppings) + " added as toppings"
    if chosen_toppings
    else ""
)

cheese_text = "with extra cheese" if extra_cheese else "without extra cheese"

combo_text = ""
if chosen_combo:
    if len(chosen_combo) == 1:
        combo_text = f"along with a {chosen_combo[0].lower()}"
    else:
        combo_text = (
            "along with "
            + ", ".join(item.lower() for item in chosen_combo[:-1])
            + f" & {chosen_combo[-1].lower()}"
        )

st.markdown("### Your Order Summary:")
st.markdown(
    f"You ordered a {base_type.lower()} {pizza.lower()} pizza {cheese_text}"
    + toppings_text
    + (" " if combo_text == "" else ", ")
    + combo_text
    + "."
)

st.markdown(f"**Total Price: ₹{total_price}**")
