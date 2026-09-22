"""Tests for temperature conversion behavior."""

import unittest

from src.temperature import celsius_to_fahrenheit


class CelsiusToFahrenheitTests(unittest.TestCase):
    def test_freezing_point(self) -> None:
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_boiling_point(self) -> None:
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_negative_value(self) -> None:
        self.assertEqual(celsius_to_fahrenheit(-40), -40)


if __name__ == "__main__":
    unittest.main()
