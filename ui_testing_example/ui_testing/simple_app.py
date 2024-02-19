import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


# Basic title for the chart
st.title('Cool chart!')

# Optionally allow the user to rename the labels using a text input
x_axis = st.text_input('X Axis label', 'some label for x here')
y_axis = st.text_input('Y Axis label', 'some label for y here')

# Generate some random data for the chart
chart_data = pd.DataFrame(
     np.random.randn(20, 2),
     columns=['a', 'b'])

# Create a very basic Altair line chart
chart = alt.Chart(chart_data).mark_line().encode(
    x=alt.X('a', title=x_axis),
    y=alt.Y('b', title=y_axis),
)

# Display the chart
st.altair_chart(chart)

# Ask the user which image to display
images = {
    'forest': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Adirondacks_in_May_2008.jpg/640px-Adirondacks_in_May_2008.jpg',
    'mountain': 'https://upload.wikimedia.org/wikipedia/commons/e/e7/Everest_North_Face_toward_Base_Camp_Tibet_Luca_Galuzzi_2006.jpg',
    'ocean': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Atlantic_near_Faroe_Islands.jpg/1200px-Atlantic_near_Faroe_Islands.jpg',
    'dessert': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Desserts.jpg/640px-Desserts.jpg',
}
image_type = st.radio('Which image should we show?', images.keys())

# Display the image
st.text(f'This is an image of {image_type}.')
st.image(images[image_type])
