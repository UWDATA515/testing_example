# Streamlit UI Testing Example

Prerequisite: install the `streamlit` and `altair` packages with the following
commands:

    conda install streamlit
    conda install altair

You can then run the example Streamlit app with the following command:

    python -m streamlit run ui_testing/simple_app.py

To run the tests, you can run the following command:

    python -m unittest discover

[More information on Streamlit's `AppTest` framework can be found in
Streamlit's documentation.](https://docs.streamlit.io/library/advanced-features/app-testing)

## Exercise

1. Make sure you can run the Streamlit app using the command
`python -m streamlit run ui_testing/simple_app.py` and play around with the
app to get a sense of what it does.

2. Take a look at the file `tests/test_simple_app.py` to see the starter test
code for the app. The test currently validates the title of the page, the
default labels for the x and y axis of the chart, and that providing input to
the text input components changes the x and y axis labels.

3. Add the following new tests:
    - A test that validates that the radio button options are 'forest', 'mountain', 'ocean', and 'dessert'
    - A test that validates that the default radio button value is 'forest'
    - A test that validates that the default text after the radio button is 'This is an image of forest.'
    - A test that interacts with the radio button to set its value to 'dessert', then validates that the text now says 'This is an image of dessert.'

4. BONUS: Only do this part after you have completed the previous section. Add a test that validates the URL of the default image (ie that it matches the expected forest image URL from the code). This is significantly harder because the `AppTest` framework does not explicitly support media elements like `st.image`. However, it is possible! See if you can figure it out. I suggest starting with the documentation, but you can also try searching within the Streamlit source code at github.com/streamlit/streamlit.

<details>
<summary>Solution for accessing the URL from the test case:</summary>

You can use the `AppTest.get()` function to return image elements using `self.at.get('imgs')`. This returns a list of images, so you need to get the first one with `[0]`. This is then an `UnknownElement`, so we can print out `element.__dict__` to see its fields. Once there, we see some stuff about "proto" and "imgs", which is then another list containing URLs. Putting it all together, we can get the image URL via the following line of code:

    cur_image_url = self.at.get('imgs')[0].proto.imgs[0].url

Whew! That was complicated! I hope Streamlit makes this testing easier in future. But the point of this exercise is that you can test a lot of user interface things, even if `AppTest` doesn't explicitly support it.
</details>
