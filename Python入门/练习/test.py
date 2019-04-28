import unittest
import Train


class Testmulit(unittest.TestCase):
    def test_notint(self):
        self.assertRaises(TypeError,
                          Train.is_multiple, 're', 'es')

    def test_True(self):
        self.assertTrue(Train.is_multiple(4, 2))

    def test_False(self):
        self.assertFalse(Train.is_multiple(2, 4))

    def test_iseven_True(self):
        self.assertTrue(Train.is_even(2312))

    def test_iseven_False(self):
        self.assertFalse(Train.is_even(2313))

    def test_minmax_Equal(self):
        self.assertEqual(Train.minmax([0, 2, 3, 75, 24, -1, 23, -9]), (-9, 75))

    def test_squaren_Equal(self):
        self.assertEqual(Train.square_n(3),14)

    def test_sumsquare_Equal(self):
        self.assertEqual(Train.sum_square(5),35)

    def test_createlist_Equal(self):
        self.assertEqual(Train.list_create(),35)

if __name__ == '__main__':
    unittest.main()
