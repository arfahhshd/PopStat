import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='PopStatExplore')
st.header('Lets Explore!!')
#st.subheader('This data include from 2010 until 2019. You can fill up the form to see the data related to you!')
st.write('This data include from 2010 until 2019. You can fill up the form to see the data related to you!')



### --- LOAD DATAFRAME
#csv_file = '(1) pop_mal.csv'
#sheet_name = 'DATA'

# Load CSV data
@st.cache_data  # Use Streamlit's caching feature for better performance
def load_data():
    data = pd.read_csv('(1)(2) pop_malaysia.csv')  # Replace 'your_file.csv' with your actual CSV file
    return data


data = load_data()

#df = pd.read_excel(excel_file,
                  # sheet_name=sheet_name,
                  # usecols='B:D',
                   #header=3)

#df = pd.read_csv(csv_file,
                   #sheet_name=sheet_name,
                   #usecols='B:D',
                   #header=3)
#st.write("""### We need some information to predict the population""" )

sex= (
        "Sex",
        "Male",
        "Female"
    )

age =(
        "Age",
        "0 to 4", 
        "5 to 9", 
        "10 to 14", 
        "15 to 19", 
        "20 to 24", 
        "25 to 29", 
        "30 to 34",
        "35 to 39", 
        "40 to 44", 
        "45 to 49", 
        "50 to 54", 
        "55 to 59", 
        "60 to 64", 
        "65 to 69",
        "70 to 74", 
        "75 to 79", 
        "80+"
    )
ethnic=(
        "Ethnics",
        "Bumiputera",
        "Chinese",
        "Indians",
        "Others"
)
#citizen=(
    #"Malaysian citizens",
    #"Non-Malaysian citizens")

sex = st.selectbox("What is your gender?", sex)
age = st.selectbox("What is your Age?", age)
ethnic = st.selectbox("What is your Ethnic?", ethnic)
#citizen= st.selectbox ("Are you a Malaysian citizen?", citizen)
year = st.slider("Years",2010, 2019, 2015)


ok = st.button("Let's go")

if ok:
    filtered_data = data[(data['Sex'] == sex) & (data['Age Group'] == age) & (data['Ethnic'] == ethnic) & (data['Year'] == year)] # (data['Citizen category'] == citizen)
    if not filtered_data.empty: 
        st.title('Data for Selected Criteria')
        st.dataframe(filtered_data)
    else:
        st.warning('No data found for the selected criteria. Please adjust your inputs.')

 # Display Filtered Data in a Styled Box
   # st.subheader('Data Related to Your Form:')
    #with st.container():  # Use beta_container for better styling options
       # st.write(
          #  f"<div style='background-color:#000000; padding: 10px; border-radius: 10px;'>"
          #  f"<p style='font-size:16px; font-weight:bold;'>Filtered Data:</p>"
          #  f"{filtered_data.to_html(index=False, classes='dataframe')}"
          #  "</div>",
         #   unsafe_allow_html=True
       # )
    