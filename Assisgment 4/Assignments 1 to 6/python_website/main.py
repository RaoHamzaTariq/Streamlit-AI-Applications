import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("General Data Analysis Dashboard")

st.subheader("Upload your dataset")
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                data = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file format. Please upload a CSV or Excel file.")
                return None
            return data
        except Exception as e:
            st.error(f"Error loading file: {e}")
            return None
    else:
        st.info("Please upload a file to get started.")
        return None

data = load_data(uploaded_file)

if data is not None:
    st.subheader("Dataset")
    st.write(data)

    st.subheader("Basic Data Analysis")

    st.write("Summary Statistics")
    st.write(data.describe())

    st.write("Correlation Matrix")
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_columns) > 0:
        corr = data[numeric_columns].corr()
        st.write(corr)
    else:
        st.warning("No numeric columns found for correlation matrix.")

    st.subheader("Data Visualization")


    st.write("Select columns for visualization")
    all_columns = data.columns.tolist()

    st.write("Scatter Plot")
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("Select X-axis", all_columns)
    with col2:
        y_axis = st.selectbox("Select Y-axis", all_columns)
    
    if x_axis and y_axis:
        fig, ax = plt.subplots()
        sns.scatterplot(x=x_axis, y=y_axis, data=data, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Please select both X-axis and Y-axis for the scatter plot.")

    st.write("Histogram")
    hist_column = st.selectbox("Select column for histogram", all_columns)
    if hist_column:
        fig, ax = plt.subplots()
        sns.histplot(data[hist_column], kde=True, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Please select a column for the histogram.")

    st.write("Box Plot")
    box_x = st.selectbox("Select X-axis (categorical)", all_columns)
    box_y = st.selectbox("Select Y-axis (numeric)", all_columns)
    if box_x and box_y:
        fig, ax = plt.subplots()
        sns.boxplot(x=box_x, y=box_y, data=data, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Please select both X-axis and Y-axis for the box plot.")