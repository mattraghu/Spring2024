def reverse(s):
    """
    Return a reversed copy of s
    Input: s - string
    Output: string 
    """
    reversed_string = ''
    # go through string and add each character to the front of the reversed string
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

def substring(target, s):
    """
    Return the index of the first occurence of target in s
    Input: target - string
           s - string
    Output: int
    """
    if target == "":
        return 0  
    target_length = len(target)
    # go through string and check if the target is equal to the substring based on the target length
    for i in range(len(s) - target_length + 1):
        if s[i:i + target_length] == target:
            return i
    return -1 

def find_second(target, s):
    """
    Return the index of the second occurence of target in s
    Input: target - string
           s - string
    Output: int
    """

    if target == "":
        return 0
    foundFirst = False
    target_length = len(target)
    # same as substring but we need to find the second occurence
    for i in range(len(s) - target_length + 1):
        if s[i:i + target_length] == target:
            if foundFirst:
                return i
            foundFirst = True
    return -1


def get_lines(path):
    """
    Generator that yields lines from a file, removing comments and joining lines ending in '\'
    Input: path - string
    Output: string
    """

    with open(path, 'r') as file:
        line_buffer = ""
        for line in file:
            stripped_line = line.rstrip('\n') # remove newline chars
            if stripped_line.endswith('\\'):
                # if ends with \ then add to line buffer
                line_buffer += stripped_line[:-1].rstrip() + ' '
            else:
                # if not then yield the full line and reset line buffer
                full_line = line_buffer + stripped_line
                line_buffer = ""  

                # remove comments
                comment_index = full_line.find('#')
                if comment_index != -1:
                    full_line = full_line[:comment_index].rstrip()
                if full_line:  # now if the line is not empty, yield it
                    yield full_line

import unittest
class TestFunctions(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("   "), "   ")

    def test_substring(self):
        self.assertEqual(substring("he", "hello"), 0)
        self.assertEqual(substring("lo", "hello"), 3)
        self.assertEqual(substring("world", "hello"), -1)
        self.assertEqual(substring("", "hello"), 0)
        self.assertEqual(substring("iss","Mississippi"), 1)

    def test_find_second(self):
        self.assertEqual(find_second("l", "hello"), 3)
        self.assertEqual(find_second("h", "hello"), -1)
        self.assertEqual(find_second("world", "hello"), -1)
        self.assertEqual(find_second("", "hello"), 0)
        self.assertEqual(find_second("iss","Mississippi"), 4)
        self.assertEqual(find_second("abba", "abbabba"), 3)

    def test_get_lines(self):
        expected = ["<line0>", "<line1>", "<line2>", "<line3.1 line3.2 line3.3>", "<line4.1 line4.2>", "<line5>", "<line6>"]
        result_lines = list(get_lines("test.txt"))
        self.assertEqual(result_lines, expected)
 
test = TestFunctions()
test.test_reverse()
test.test_substring()
test.test_find_second()
test.test_get_lines()