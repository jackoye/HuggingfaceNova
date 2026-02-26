# test_huggingfacenova.py
"""
Tests for HuggingfaceNova module.
"""

import unittest
from huggingfacenova import HuggingfaceNova

class TestHuggingfaceNova(unittest.TestCase):
    """Test cases for HuggingfaceNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HuggingfaceNova()
        self.assertIsInstance(instance, HuggingfaceNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HuggingfaceNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
