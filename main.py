import streamlit as st
import pandas as pd 

# to show all environments - pip included:
# conda list env 

# to show all environments on conda:
# conda env list

header = st.container()
dataset = st.container()
features = st.container()  
model_training = st.container()
image = st.container()

with header:
	st.title('Welcome to my awesome data science project')
	st.text('In this project I looked into the transactions of taxis in NYC')

with dataset:
	st.header('NYC taxi dataset')
	st.text('I found this dataset on _.com')

	taxi_data = pd.read_csv('data/taxi_data.csv')
	st.write(taxi_data.head())

	st.subheader('Pick-up location ID distribution on the nyc dataset')
	pulocation_dist = pd.DataFrame(taxi_data['PULocationID'].value_counts()).head(50)
	st.bar_chart(pulocation_dist)

with features:
	st.header('The features I created')

	st.markdown('* **first feature:** I created this feature because of this ... calculated using this logic')
	st.markdown('* **second feature:** I created this feature because of this ... calculated using this logic')

with model_training:
	st.header('Time to train the model')
	st.text("Choose the hyper parameters and run model")

	sel_col, disp_col = st.columns(2)
	max_depth = sel_col.slider('What should be the max_depth of the model?', min_value=10, max_value=100, value=20, step=10)

	n_estimators = sel_col.selectbox('How manu trees should there be', options=[100,200,300,'No Limit'], index = 0) # default value should be index 0 of list

	input_feature = sel_col.text_input('Which feature should be used as the input feature?', 'PULocationID')

with image:
	st.image("data/image.png")


