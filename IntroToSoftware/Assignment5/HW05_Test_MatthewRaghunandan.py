from HW05_MatthewRaghunandan import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, reorder

import unittest

class TestFunctions(unittest.TestCase):
    def test_list_copy(self):
        self.assertEqual(list_copy([1, 2, 3]), [1, 2, 3])
        self.assertEqual(list_copy([]), [])
        self.assertEqual(list_copy(['a', 'b', 'c']), ['a', 'b', 'c'])
        self.assertEqual(list_copy([1, 'a', 2, 'b']), [1, 'a', 2, 'b'])

    def test_list_intersect(self):
        self.assertEqual(list_intersect([1, 2, 3], [2, 3, 4]), [2, 3])
        self.assertEqual(list_intersect([], [1, 2, 3]), [])
        self.assertEqual(list_intersect([1, 2, 3], []), [])
        self.assertEqual(list_intersect([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(list_intersect([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_list_difference(self):
        self.assertEqual(list_difference([1, 2, 3], [2, 3, 4]), [1])
        self.assertEqual(list_difference([], [1, 2, 3]), [])
        self.assertEqual(list_difference([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(list_difference([1, 2, 3], [4, 5, 6]), [1, 2, 3])
        self.assertEqual(list_difference([1, 2, 3], [1, 2, 3]), [])

    def test_remove_vowels(self):
        self.assertEqual(remove_vowels('Matthew is cool'), 'Matthew cool')
        self.assertEqual(remove_vowels('a e i o u'), '')
        self.assertEqual(remove_vowels('aeiou'), '')
        self.assertEqual(remove_vowels(''), '')

    def test_check_pwd(self):
        self.assertTrue(check_pwd('1AppleSauce'))
        self.assertFalse(check_pwd('AppleSauce'))
        self.assertFalse(check_pwd(''))
        self.assertFalse(check_pwd('1a'))

    def test_reorder(self):
        self.assertEqual(reorder([3, 2, 1]), [1, 2, 3])
        self.assertEqual(reorder([1, 2, 3]), [1, 2, 3])
        self.assertEqual(reorder([1, 3, 2]), [1, 2, 3])
        self.assertEqual(reorder([1]), [1])
        self.assertEqual(reorder([]), [])

test = TestFunctions()
unittest.main(exit=False)

test.test_list_copy()
test.test_list_intersect()
test.test_list_difference()
test.test_remove_vowels()
test.test_check_pwd()
test.test_reorder()




        



