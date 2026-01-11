import unittest

from get_city_country import get_city_country


class CityTestCase(unittest.TestCase):
    """Tests for 'get_city_country.py'."""

    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        city_country = get_city_country("santiago", "chile")
        self.assertEqual(city_country, "Santiago, Chile")

    def test_city_country_population(self):
        """Do cities like 'Santiago, Chile - population 5000000' work?"""
        city_country = get_city_country("santiago", "chile", population=5000000)
        self.assertEqual(city_country, "Santiago, Chile - population 5000000")


if __name__ == "__main__":
    unittest.main()
