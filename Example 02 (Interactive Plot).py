

'''
Description about Example:

In this Streamlit app provides an interactive plot where users can choose a range for the x-axis, and it dynamically 
generates and displays a line chart showing the squares of the selected x-values. It's a simple example of how 
Streamlit can be used to create web applications with interactive data visualizations.

'''
import streamlit as st
import plotly.express as px

# This line sets the title of your Streamlit web application to "Interactive Plot Example," 
# which is displayed at the top of the web page.
st.title("Interactive Plot Example")

# User input
# Here, a slider widget is created using st.slider(). This widget allows the user to select a 
# range of values for the variable x. The slider ranges from 0 to 10, and the initial selected range is set to (3, 7).
x = st.slider("Select a range for x:", 0, 10, (3, 7))

'''
Create a dynamic plot
This section creates a dynamic plot using Plotly Express. It generates a line chart (px.line) where the x-axis values 
are generated as a list using range(x[0], x[1] + 1) based on the user's slider input, and the y-axis values are 
calculated as squares of the x-values. So, it creates a line chart of x^2.
'''
fig = px.line(x=list(range(x[0], x[1] + 1)), y=[x**2 for x in range(x[0], x[1] + 1)])

# Finally, the st.plotly_chart() function is used to display the Plotly Express figure (fig) in the Streamlit app. 
st.plotly_chart(fig)