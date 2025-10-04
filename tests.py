import unittest
import conversions

class TestCelsiusConversions(unittest.TestCase):

  def test_convertCelsiusToKelvin(self):
    test_cases = [(0, 273.15), (100, 373.15), (-273.15, 0), (300, 573.15), (25, 298.15)]
    for c, expected in test_cases:
      result = conversions.convertCelsiusToKelvin(c)
      self.assertAlmostEqual(result, expected, places=2, msg=f"{c}C should be {expected}K")

  def test_convertCelsiusToFahrenheit(self):
    test_cases = [(0, 32), (100, 212), (-40, -40), (300, 572), (25, 77)]
    for c, expected in test_cases:
        result = conversions.convertCelsiusToFarenheit(c)
        self.assertAlmostEqual(result, expected, places=2, msg=f"{c}C should be {expected}F")

if __name__ == "__main__":
    unittest.main()
