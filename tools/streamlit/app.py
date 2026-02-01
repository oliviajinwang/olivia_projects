import streamlit as st
import pandas as pd

# 1. Add a title and header
st.title("My First Streamlit App")
st.header("Interactive Data Dashboard")

st.sidebar.write("Hello")

# 2. Add some text
st.write("Hello! This is a simple app to show how Streamlit works.")

# 3. Create a simple interaction
name = st.text_input("What is your name?")
if name:
    st.write(f"Welcome to the app, **{name}**!")

# 4. Add a slider and display data
age = st.slider("Select a value", 0, 100, 25)
st.write(f"You selected: {age}")

# 5. Show a simple chart
chart_data = pd.DataFrame([age*0.5, age, age*2], columns=["Numbers"])
st.line_chart(chart_data)

# Try out button
if st.button("Say Hello"):
    st.success("Hello there! You clicked the button.")
    st.balloons() # Adds a celebratory animation
else:
    st.write("Click the button to see what happens.")

# The variable 'show_details' will be True if checked, False if not
show_details = st.checkbox("Show technical details")

if show_details:
    st.write("### Technical Specifications")
    st.code("""
    Model: GPT-4o
    Latency: 200ms
    Status: Operational
    """)
else:
    st.write("Check the box above to see the specs.")


# Creating the selectbox
fruits = ["Apple", "Banana", "Cherry", "Dragonfruit"]
choice = st.selectbox("What is your favorite fruit?", options=fruits)
st.write(f"You selected: {choice}")