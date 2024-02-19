# Mocking Example

This simple example demonstrates how you might use Python's unittest mocking
framework in your testing.

The code in `google/doodle.py` determines whether there is a "doodle of the
day" on Google today, and either returns the title of it or `None`.  You can
run the example with the following command:

    python -m google.doodle

This code presents a problem when writing a test - because on a given day,
either there's a specific doodle, or there isn't one, and we can't write a
test that will work every day if it's submitting a request to Google. The
solution is to *mock* the request to Google. We will replace the
`requests.get` function with a fake implementation that will allow us to
return exactly the data that we want - or raise an error! HTTP requests are
prime examples for mocking, although you can use mocks any time to make sure
that you are testing ONLY what you want to test.

[Read more about unittest mocking in Python's documentation.](https://docs.python.org/3/library/unittest.mock.html)

## Exercise

1. Make sure you can run the code with `python -m google.doodle`.

2. Take a look at the file `tests/test_doodle.py` to see the starter test
code for the app. The test currently validates that the function returns the
doodle name from a simplified version of the Google homepage (with a custom
doodle), using a mock. You can run the test with the following command:

        python -m unittest discover

3. Add the following new tests:
    - A test that validates that the `load_google_doodle_title` function calls `requests.get` with the argument `https://google.com`. Look at the [`assert_called_with`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with) function in the Python mocking documentation.
    - A test that validates that if there is no text in the response, the function returns `None`.
    - A test that validates that if the `twitter:title` meta content tag is missing, the function returns `None`.
    - A test that validates that the function returns `None` if the request raises a timeout error. Check out the [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect) option for how to raise an error in a mock. The exception that should be raised is from the `requests` package: `requests.exceptions.Timeout`.
