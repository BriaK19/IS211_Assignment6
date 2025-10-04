import unittest
import conversions
import conversions_refactored as cref

class TestCelsiusConversions(unittest.TestCase):

  def test_convertCelsiusToKelvin(self):
    test_cases = [(0, 273.15), (100, 373.15), (-273.15, 0), (300, 573.15), (25, 298.15)]
    for c, expected in test_cases:
      result = conversions.convertCelsiusToKelvin(c)
      self.assertAlmostEqual(result, expected, places=2, msg=f"{c}C should be {expected}K")

  def test_convertCelsiusToFahrenheit(self):
    test_cases = [(0, 32), (100, 212), (-40, -40), (300, 572), (25, 77)]
    for c, expected in test_cases:
        result = conversions.convertCelsiusToFahrenheit(c)
        self.assertAlmostEqual(result, expected, places=2, msg=f"{c}C should be {expected}F")

if __name__ == "__main__":
    unittest.main()

import conversions_refactored as cref

class TestRefactoredConversions(unittest.TestCase):

    def test_temperature_conversions(self):
        self.assertAlmostEqual(cref.convert("celsius", "kelvin", 0), 273.15)
        self.assertAlmostEqual(cref.convert("fahrenheit", "celsius", 32), 0)
        self.assertAlmostEqual(cref.convert("kelvin", "fahrenheit", 273.15), 32)

    def test_distance_conversions(self): 
        self.assertAlmostEqual(cref.convert("miles", "meters", 1), 1609.34)
        self.assertAlmostEqual(cref.convert("yards", "meters", 1), 0.9144)

    def test_same_unit(self):
        self.assertEqual(cref.convert("meters", "meters", 10), 10)
        self.assertEqual(cref.convert("celsius", "celsius", 100), 100)

    def test_incompatible_units(self):
        with self.assertRaises(cref.ConversionNotPossible):
            cref.convert("celsius", "meters", 100)


