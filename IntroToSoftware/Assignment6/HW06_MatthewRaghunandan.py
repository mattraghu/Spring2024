from collections import defaultdict
from collections import Counter

def anagrams_lst(st1, st2):
    st1 = list(st1)
    st2 = list(st2)
    st1.sort()
    st2.sort()

    if st1 == st2:
        return True
    else:
        return False
    

def anagrams_dd(st1, st2):
    dd = defaultdict(int)
    for char in st1:
        dd[char] += 1
    for char in st2:
        if char in dd:
            dd[char] -= 1
        else:
            return False
    
    return all(value == 0 for value in dd.values())

def anagrams_cntr(st1, st2):
    return Counter(st1) == Counter(st2)


def covers_alphabet(sentence):
    sentence = sentence.lower()
    sentence = set(sentence)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    if alphabet.issubset(sentence):
        return True
    else:
        return False
    

import unittest

class TestHW6(unittest.TestCase):
    def test_anagrams_lst(self):
        self.assertEqual(anagrams_lst('listen', 'silent'), True)
        self.assertEqual(anagrams_lst('triangle', 'integral'), True)
        self.assertEqual(anagrams_lst('cat', 'dog'), False)

    def test_anagrams_dd(self):
        self.assertEqual(anagrams_dd('listen', 'silent'), True)
        self.assertEqual(anagrams_dd('triangle', 'integral'), True)
        self.assertEqual(anagrams_dd('cat', 'dog'), False)

    def test_anagrams_cntr(self):
        self.assertEqual(anagrams_cntr('listen', 'silent'), True)
        self.assertEqual(anagrams_cntr('triangle', 'integral'), True)
        self.assertEqual(anagrams_cntr('cat', 'dog'), False)

    def test_covers_alphabet(self):
        self.assertEqual(covers_alphabet('The quick, brown, fox; jumps over the lazy dog!'), True)
        self.assertEqual(covers_alphabet('the quick brown fox jumped over the lazy dog'), False)
        self.assertEqual(covers_alphabet('the quick brown fox jumps over the lazy cat'), False)

test = TestHW6()
test_suite = unittest.TestLoader().loadTestsFromModule(test)
unittest.TextTestRunner().run(test_suite)
