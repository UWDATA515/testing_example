"""
In addition to testing Python logic, it's always a good idea to test
the user interface components of an application. There are many ways
to accomplish this, depending on the user interface framework you are
using. The example here applies to the Streamlit framework, which
provides a native app testing framework.

More information in Streamlit's documentation:
https://docs.streamlit.io/library/advanced-features/app-testing
"""

from json import loads
import unittest

from streamlit.testing.v1 import AppTest


class SimpleAppTest(unittest.TestCase):
    def setUp(self):
        """
        The unittest framework automatically runs this `setUp` function before
        each test. By refactoring the creation of the AppTest into a common
        function, we reduce the total amount of code in the file.
        """
        self.at = AppTest.from_file('ui_testing/simple_app.py').run()

    def test_tile(self):
        self.assertEqual(self.at.title[0].value, 'Cool chart!')

    def test_chart_axis(self):
        chart = self.at.get('arrow_vega_lite_chart')[0]
        spec = loads(chart.spec)['encoding']
        self.assertEqual(spec['x']['title'], 'some label for x here')
        self.assertEqual(spec['y']['title'], 'some label for y here')

    def test_renaming_axes(self):
        self.at.text_input[0].input("What I want").run()
        self.at.text_input[1].input("What I have").run()
        chart = self.at.get('arrow_vega_lite_chart')[0]
        spec = loads(chart.spec)['encoding']
        self.assertEqual(spec['x']['title'], 'What I want')
        self.assertEqual(spec['y']['title'], 'What I have')
