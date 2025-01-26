import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#set page config
st.set_page_config(page_title="Data Visualizer",layout="centered",page_icon="📊")

#title                                                                                                                                                           
st.title("📊Data Visualiser Web App")

#getting the working directory of ram.py file
working_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = f"{working_dir}/data"

#List all the files we have in the "data" folder
files  = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

#dropdown
select_file = st.selectbox("Please Select a File",files,index=None)


if select_file:

#get the complete path of selected file
       file_path = os.path.join(folder_path,select_file)

#Read the csv filee
       df = pd.read_csv(file_path)

       col1,col2 = st.columns(2)

       column_names = df.columns.to_list()

       with col1:
        st.write("")
        st.write(df.head())

       with col2:
       #user selection for df of columns
          x_axis = st.selectbox("Select the X-axis", options=column_names + ["None"])
          y_axis = st.selectbox("Select the Yaxis", options=column_names + ["None"])

       plot_list =["Line Plot","Bar Chart","Scatter Plot","Disturbution Plot","Count Plot"]

       select_plot = st.selectbox("Select a Plot",options=plot_list,index=None)


#Button to generate plots
if st.button("Generate Plot"):
       fig,ax = plt.subplots(figsize=(6,4))

       if select_plot == "Line Plot":
              sns.lineplot(x=df[x_axis],y=df[y_axis] , ax=ax)
       
       elif select_plot == "Bar Chart":
              sns.barplot(x=df[x_axis],y=df[y_axis] , ax=ax)

       elif select_plot == "Scatter Plot":
              sns.scatterplot(x=df[x_axis],y=df[y_axis] , ax=ax)

       elif select_plot == "Disturbution Plot":
              sns.histplot(x=df[x_axis],kde=True,ax=ax)

       elif select_plot == "Count Plot":
              sns.countplot(x=df[x_axis],y=df[y_axis] , ax=ax)

#Adjust Labels
       ax.tick_params(axis="x",labelsize=10)
       ax.tick_params(axis="y",labelsize=10)
       
       #title axes labels
       plt.title(f"{select_plot}of {y_axis} vs {x_axis}",fontsize=12)
       plt.xlabel(x_axis,fontsize=10)
       plt.xlabel(y_axis,fontsize=10)

       st.pyplot(fig)