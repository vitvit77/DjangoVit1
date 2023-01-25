from django.test import TestCase

class MainTestCase(TestCase):
    def test_something(self):
        self.assertEqual(True, True)

class MainTestCase1(TestCase):
    def test_something(self):
        self.assertEqual(1, 1)

