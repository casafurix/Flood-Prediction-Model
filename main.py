import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Visualisation", page_icon=":bar_chart:", layout="wide")
st.title("Exploratory Data Analysis")

dataset_name =  st.sidebar.selectbox("Select Dataset", ("Rainfall in India (1901-2015)", "Kerala Rainfall (1901-2018)"))


India = pd.read_csv("A://Projects//Flood Prediction Model//Datasets//rainfall_in_india_1901-2015.csv")
Kerala = pd.read_csv("A:\Projects\Flood Prediction Model\Datasets\kerala.csv")

def init_dataset(dataset_name):
    if (dataset_name == "Rainfall in India (1901-2015)"):
        init_data = st.dataframe(India)
    elif (dataset_name == "Kerala Rainfall (1901-2018)"):
        init_data = st.dataframe(Kerala)
    print(init_data)

def plot_missing(dataset_name):
    if (dataset_name == "Rainfall in India (1901-2015)"):
        data = st.dataframe(India)
        total = data.isnull().sum().sort_values(ascending=False)
        percent = (data.isnull().sum()/data.isnull().count()).sort_values(ascending=False)
        missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
        f, ax = plt.subplots(figsize=(15, 6))
        plt.xticks(rotation='90')
        sns.barplot(x=missing_data.index, y=missing_data['Percent'])
        plt.xlabel('Features', fontsize=15)
        plt.ylabel('Percent of missing values', fontsize=15)
        plt.title('Percent missing data by feature', fontsize=15)
        missing_data.head()








def final_dataset(dataset_name):
    if (dataset_name == "Rainfall in India (1901-2015)"):
        India['JAN'].fillna((India['JAN'].mean()), inplace=True)
        India['FEB'].fillna((India['FEB'].mean()), inplace=True)
        India['MAR'].fillna((India['MAR'].mean()), inplace=True)
        India['APR'].fillna((India['APR'].mean()), inplace=True)
        India['MAY'].fillna((India['MAY'].mean()), inplace=True)
        India['JUN'].fillna((India['JUN'].mean()), inplace=True)
        India['JUL'].fillna((India['JUL'].mean()), inplace=True)
        India['AUG'].fillna((India['AUG'].mean()), inplace=True)
        India['SEP'].fillna((India['SEP'].mean()), inplace=True)
        India['OCT'].fillna((India['OCT'].mean()), inplace=True)
        India['NOV'].fillna((India['NOV'].mean()), inplace=True)
        India['DEC'].fillna((India['DEC'].mean()), inplace=True)
        India['ANNUAL'].fillna((India['ANNUAL'].mean()), inplace=True)
        India['Jan-Feb'].fillna((India['Jan-Feb'].mean()), inplace=True)
        India['Mar-May'].fillna((India['Mar-May'].mean()), inplace=True)
        India['Jun-Sep'].fillna((India['Jun-Sep'].mean()), inplace=True)
        India['Oct-Dec'].fillna((India['Oct-Dec'].mean()), inplace=True)
        data = st.dataframe(India)
    elif (dataset_name == "Kerala Rainfall (1901-2018)"):
        data = st.dataframe(Kerala)
    print(data)

st.write("Initial, Raw Dataset:")
init_dataset(dataset_name)

st.write("Missing Values:")
plot_missing(dataset_name)

st.write("Final, Cleaned Dataset:")
final_dataset(dataset_name)