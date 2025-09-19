import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Daniel\Desktop\Workshop\Chatbot_V2\pages\Melbourne.csv')
df['Price'].fillna(0, inplace=True)

tab1, tab2, tab3 = st.tabs(['Data Overview','Visualization','Solutions'])
with tab1:
    st.subheader('Dataset Overview')
    st.write(f'Data Shape: {df.shape}')
    st.dataframe(df.head(10))

    st.subheader('Select Columns')
    select_columns = st.multiselect("Select Columns : ", df.columns.tolist(),default=df.columns.tolist())
    st.dataframe(df[select_columns])

    st.subheader("Filter By Price")
    price = st.slider("Minimum price",(df['Price'].min()),(df['Price'].max()))
    filtered_price = df[df['Price']>= price]
    st.write(f"Price Range >= {price}")
    st.dataframe(filtered_price)

with tab2:
    st.header("Visualizations")
    st.bar_chart(df['Price'].head(30))

    # x = df['Price']
    # y = df['Rooms']
    min_price, max_price = st.slider("slider",
    int(df['Price'].min()), 
    int(df['Price'].max()),
    (int(df['Price'].min()), int(df['Price'].max())
    ))
    
    filt_data = df[(df['Price'] > min_price & (df['Price'] <= max_price))]
    xpoints = df['Price']
    ypoints = df['Rooms'].head(10)

    fig, ax = plt.subplots()
    ax.hist(df['Price'].dropna(),  bins = 20, alpha = 0.7, color = 'red')
    ax.set_title('Price / Rooms relation')
    ax.set_xlabel('Price')
    ax.set_ylabel('Rooms')

    st.pyplot(fig)


with tab3:
    st.map(df.rename(columns={'Lattitude':'LAT','Longtitude':'LON'}))