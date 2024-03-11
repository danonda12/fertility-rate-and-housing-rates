import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to generate sample data
def generate_data():
    years = np.arange(2000, 2023)
    fertility_rates = np.random.uniform(low=1.5, high=2.5, size=len(years))
    average_home_prices = np.random.uniform(low=200000, high=600000, size=len(years))
    return pd.DataFrame({'Year': years, 'Fertility Rate': fertility_rates, 'Average Home Price': average_home_prices})

data = generate_data()

# Introduction section
st.title('The Connection Between Fertility Rates and Housing Market Trends')
st.write('''
This app explores how changes in fertility rates impact the housing market, 
including the demand for different types of homes and overall market dynamics.
''')
st.sidebar.markdown("**Note:** This app uses simulated data for demonstration purposes.")
# Fertility Rates Overview
st.header('Fertility Rates Overview')
fig, ax = plt.subplots()
ax.plot(data['Year'], data['Fertility Rate'], marker='o', linestyle='-')
ax.set_xlabel('Year')
ax.set_ylabel('Fertility Rate')
ax.set_title('Fertility Rate Over Time')
st.pyplot(fig)

# Housing Market Dynamics
st.header('Housing Market Dynamics')
fig, ax = plt.subplots()
ax.plot(data['Year'], data['Average Home Price'], color='red', marker='x', linestyle='-')
ax.set_xlabel('Year')
ax.set_ylabel('Average Home Price ($)')
ax.set_title('Average Home Price Over Time')
st.pyplot(fig)

# Conclusion and Implications
st.header('Conclusion and Implications')
st.write('''
The declining fertility rate has significant implications for the housing market, 
influencing the types of homes in demand and overall market trends. Real estate professionals 
and policymakers need to consider these factors when planning for the future.
''')

