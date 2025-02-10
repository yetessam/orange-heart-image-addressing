# test/test_nav_plugin.py
import unittest

from loguru import logger
from ..htmlprocessor import HTMLProcessor
from ..plugins.navigation.plugin import NavPlugin

class TestNavPlugin(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment.
        """
        # Create a mock logger (you can use a real logger if needed)
        self.logger = unittest.mock.Mock()
        
        # Create a mock HTMLProcessor instance
        self.parent = unittest.mock.Mock(spec=HTMLProcessor)
        self.parent.filepath = "test.html"
        self.parent.logger = self.logger

        # Instantiate the NavPlugin with the mock parent
        self.plugin = NavPlugin(parent=self.parent)

    def test_process(self):
        """
        Test the process method of NavPlugin.
        """
        # Define sample HTML content
        sample_content = "<html><body><nav></nav></body></html>"
        
        # Call the process method
        result = self.plugin.process(sample_content)
        
        # Assert that the result is as expected
        self.assertIn("<nav>", result)  # Example assertion
        self.assertIn("</nav>", result)  # Example assertion

    def test_process_with_no_nav(self):
        """
        Test the process method when the input HTML has no <nav> tag.
        """
        # Define sample HTML content without a <nav> tag
        sample_content = "<html><body></body></html>"
        
        # Call the process method
        result = self.plugin.process(sample_content)
        
        # Assert that the result is unchanged
        self.assertEqual(result, sample_content)

if __name__ == "__main__":
    unittest.main()