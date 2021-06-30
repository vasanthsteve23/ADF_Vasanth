from .views import age_validation
import unittest

# Create your tests here.
class TestUser(unittest.TestCase):
    def test1(self):
        """First test case"""
        result = age_validation("male",21)
        assert result == 'Eligible'

