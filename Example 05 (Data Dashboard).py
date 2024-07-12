
'''
Description about the Example:
In this Streamlit dashboard, you can:

1. Load the Iris dataset from scikit-learn.

2. Filter the data by selecting specific species using the sidebar.

3. Display the filtered dataset and provide a data summary. Visualize the data with interactive pair plots, box plots, 
scatter plots, histograms, and a correlation heatmap.

4. Customize the dashboard title, description, and footer with your own information.

Simply replace "Your Name" with your desired name at the bottom of the code. When you run this code, it will create 
an interactive data dashboard for the Iris dataset using Streamlit.
'''


import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris

# Set page title and description
st.title("Iris Dataset Dashboard")
st.write("Explore the Iris dataset with interactive visualizations.")

# Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data["target"] = iris.target
data["species"] = data["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

# Display the dataset
st.subheader("Iris Dataset Overview")
st.dataframe(data)

# Sidebar filters
st.sidebar.header("Data Filters")
species_to_filter = st.sidebar.multiselect("Select species:", data["species"].unique(), default=["setosa"])
filtered_data = data[data["species"].isin(species_to_filter)]

# Data Summary
st.sidebar.subheader("Data Summary")
st.sidebar.write(f"Number of samples: {len(filtered_data)}")
st.sidebar.write(f"Selected Species: {', '.join(species_to_filter)}")

# Pair Plot
st.header("Pair Plot")
fig = px.scatter_matrix(
    filtered_data,
    dimensions=filtered_data.columns[:-2],  # Exclude 'target' and 'species' columns
    color="species",
)
st.plotly_chart(fig)

# Box Plot
st.header("Box Plot")
fig = px.box(
    filtered_data,
    x="species",
    y="sepal length (cm)",
    color="species",
)
st.plotly_chart(fig)

# Scatter Plot
st.header("Scatter Plot")
x_axis = st.selectbox("Select X-axis feature:", data.columns[:-1])
y_axis = st.selectbox("Select Y-axis feature:", data.columns[:-1])
fig = px.scatter(
    filtered_data,
    x=x_axis,
    y=y_axis,
    color="species",
)
st.plotly_chart(fig)

# Histogram
st.header("Histogram")
selected_feature = st.selectbox("Select a feature:", data.columns[:-1])
fig = px.histogram(
    filtered_data,
    x=selected_feature,
    color="species",
    marginal="rug",
)
st.plotly_chart(fig)

# Correlation Heatmap
st.header("Correlation Heatmap")
correlation_matrix = filtered_data.corr()
fig = px.imshow(correlation_matrix, color_continuous_scale="Viridis")
st.plotly_chart(fig)


# Footer
st.sidebar.markdown("Created by Your Name")
