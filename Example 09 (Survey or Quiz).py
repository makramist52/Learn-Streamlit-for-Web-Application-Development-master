
# Survey or Quiz App: Build a survey or quiz application with multiple-choice questions.

import streamlit as st

st.title("Survey or Quiz App")

# Define questions and choices
questions = [
    "What is the capital of France?",
    "Which planet is known as the 'Red Planet'?",
    "How many continents are there?",
]

choices = [
    ["Paris", "Berlin", "Madrid", "Rome"],
    ["Mars", "Venus", "Jupiter", "Saturn"],
    ["5", "6", "7", "8"],
]

# Initialize scores
scores = [0] * len(questions)

# Display questions and collect user answers
for i, question in enumerate(questions):
    st.write(f"**Question {i + 1}:** {question}")
    selected_option = st.radio("Select an option:", choices[i])
    if selected_option == choices[i][0]:
        scores[i] = 1

# Calculate and display the final score
final_score = sum(scores)
st.write(f"Your Score: {final_score}/{len(questions)}")

