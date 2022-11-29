import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import webbrowser

# Page configuration
st.set_page_config(page_title='Archdaily statistics')
st.title('Archdaily statistics')

col1, col2 = st.columns([1, 1])

# Open csv data, get number of projects
df = pd.read_csv('projects.csv')
size = df.shape[0]

# Define data to display
metrics = col1.radio('Metrics to display', ['year', 'architect', 'country'])
plot_type = col2.radio('Plot type', ['bar', 'pie'])

# Plot type base on radio button input from user
if plot_type == 'bar':
    fig = px.histogram(df, x = metrics, text_auto=True)
    fig.update_traces(marker=dict(color='rgb(0, 150, 255)'))
    fig.update_layout(bargap=0.2)
    st.plotly_chart(fig)
else:    
    fig = px.pie(df, names = metrics)
    fig.update_traces(textposition='inside', textinfo = 'value')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    st.plotly_chart(fig)

# Display data frame 
st.dataframe(df)    
st.success('Showing ' + str(size) + ' projects from dataset')

# Redirect to project page on archdaily.com (for now only localhost)
input = st.text_input('Project id from the table', 'paste id here')
if st.button('Open project on ArchDaily'):
    webbrowser.open_new_tab('https://www.archdaily.com/' + str(input))

# Download data as csv
with open('projects.csv') as f:
    st.download_button(label = 'Download csv', data = df.to_csv(), mime = 'text/csv', file_name = 'results.csv')