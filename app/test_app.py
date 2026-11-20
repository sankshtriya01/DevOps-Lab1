import unittest
from app import greet


class TestGreeting(unittest.TestCase):

    def test_greet_returns_expected_message(self):
        self.assertEqual(
            greet("Student"),
            "Hello, Student! Welcome to DevOps Lab 1."
        )

    def test_greet_with_custom_name(self):
        self.assertEqual(
            greet("DevOps"),
            "Hello, DevOps! Welcome to DevOps Lab 1."
        )


if __name__ == "__main__":
    unittest.main()
