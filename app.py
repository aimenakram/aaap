import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from Google Drive
from google.colab import drive 
drive.mount('/content/gdrive')
url = "https://raw.githubusercontent.com/iammustafatz/diabetes-prediction-dataset/main/diabetes_prediction_dataset.csv"
df = pd.read_csv('gdrive/My Drive/diabetes_prediction_dataset.csv')

# Streamlit app code
st.title("Dataset Visualization")

# Display the dataset as a table
st.write(df)

# Visualize gender distribution
st.subheader("Gender Distribution")
gender_counts = df['gender'].value_counts()
st.bar_chart(gender_counts)

# Visualize age distribution
st.subheader("Age Distribution")
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='age', bins=20)
st.pyplot()

# Visualize correlation between variables
st.subheader("Correlation Heatmap")
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
st.pyplot()
