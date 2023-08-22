import unittest
from kmap import convert_input, mapping_terms, plotting_zero

class TestKMapFunctions(unittest.TestCase):

    def test_convert_input(self):
        input_str = "0 1 2 3 4 5"
        expected_output = ['0', '45', '2', '3', '4', '5']
        self.assertEqual(convert_input(input_str), expected_output)

    def test_mapping_terms(self):
        k_map = ['0', '45', '3', '2', '4', '5', '7', '6', '12', '13', '15', '14', '8', '9', '11', '10']
        minterms = ['0', '2', '4', '5']
        char = 1
        expected_output = [1, '45', '3', 1, 1, 1, '7', '6', '12', '13', '15', '14', '8', '9', '11', '10']
        mapping_terms(k_map, minterms, char)
        

        self.assertListEqual(k_map, expected_output)

    def test_plotting_zero(self):
        k_map = [1, '45', '3', 1, 1, 'x', '7', '6', 'x', '13', '15', '14', '8', '9', '11', '10']
        expected_output = [1, 0, 0, 1, 1, 'x', 0, 0, 'x', 0, 0, 0, 0, 0, 0, 0]
        

        self.assertListEqual(plotting_zero(k_map), expected_output)

if __name__ == '__main__':
    unittest.main()
