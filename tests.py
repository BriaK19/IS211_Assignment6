import unittest
import conversions
import conversions_refactored as cref

class TestConversions(unittest.TestCase):
    pass

class TestRefactoredConversions(unittest.TestCase):
    
    def test_tempature_all_pairs(self):
        cases = [
            ("celsius", "kelvin", 0, 273.15),
            ("celsius", "fahrenheit", 100, 212),
            ("fahrenheit", "celsius", 32, 0),
            ("fahrenheit", "kelvin", -40, 233.15),
            ("kelvin", "celsius", 273.15, 0),
            ("kelvin", "fahrenheit", 373.15, 212),
        ]
        for f, t, v, expected in cases:
            self.assertAlmostEqual(cref.convert(f, t, v), expected, places=2)

    def test_distance_all_pairs(self):
        cases = [
            ("miles", "meters", 1, 1609.34),
            ("meters", "miles", 1609.34, 1),
            ("yards", "meters", 1, 0.9144),
            ("meters", "yards", 1, 1.09361),
            ("miles", "yards", 1, 1760),
        ]
        for f, t, v, expected in cases:
            self.assertAlmostEqual(cref.convert(f, t, v), expected, places=4)

    def test_same_unit_returns_same_value(self):
        for u in ["celsius", "fahrenheit", "kelvin", "miles", "yards", "meters"]:
            self.assertEqual(cref.convert(u, u, 123.456), 123.456)

    def test_incompatible_units_raise(self):
        with self.assertRaises(cref.ConversionNotPossible):
            cref.convert("celsius", "meters", 10)

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

  def test_convertFahrenheitToCelsius(self):
    test_cases = [(32, 0), (212, 100), (-40, -40), (77, 25), (572, 300)]
    for f, expected in test_cases:
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(f), expected, places=2)

  def test_convertFahrenheitToKelvin(self):
    test_cases = [(32, 273.15), (212, 373.15), (-40, 233.15), (77, 298.15), (572, 573.15)]
    for f, expected in test_cases:
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(f), expected, places=2)

  def test_convertKelvinToCelsius(self):
    test_cases = [(273.15, 0), (373.15, 100), (0, -273.15), (298.15, 25), (573.15, 300)]
    for k, expected in test_cases:
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(k), expected, places=2)

  def test_convertKelvinToFahrenheit(self):
    test_cases = [(273.15, 32), (373.15, 212), (0, -459.67), (298.15, 77), (573.15, 572)]
    for k, expected in test_cases:
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(k), expected, places=2)

class TestRefactoredConversions(unittest.TestCase):

    def test_temperature_conversions(self):
        self.assertAlmostEqual(cref.convert("celsius", "kelvin", 100), 373.15)
        self.assertAlmostEqual(cref.convert("fahrenheit", "celsius", 32), 0)
        self.assertAlmostEqual(cref.convert("kelvin", "fahrenheit", 273.15), 32)

    def test_distance_conversions(self): 
        self.assertAlmostEqual(cref.convert("miles", "meters", 1), 1609.34, places=2)
        self.assertAlmostEqual(cref.convert("yards", "meters", 1), 0.9144, places=2)
        self.assertAlmostEqual(cref.convert("meters", "yards", 1), 1.09361, places=2)

    def test_same_unit(self):
        self.assertEqual(cref.convert("meters", "meters", 10), 10)
        self.assertEqual(cref.convert("celsius", "celsius", 50), 50)

    def test_incompatible_units(self):
        with self.assertRaises(cref.ConversionNotPossible):
            cref.convert("celsius", "meters", 100)

if __name__ == "__main__":
    unittest.main()


