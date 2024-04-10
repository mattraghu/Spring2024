import unittest

def web_analyzer(weblogs):
    webpages = {} 
    for log in weblogs: 
        if not log[1] in webpages:
            webpages[log[1]] = set([ log[0] ])
            continue
        webpages[log[1]].add(log[0])

    return sorted([(k, sorted(list(v))) for k, v in webpages.items()])





class TestWebAnalyzer(unittest.TestCase): 
    def test_web_analyzer(self):
        weblogs1 = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), 
        ]
        summary1= [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), 
        ]

        weblogs2 = [
            ('Matthew', 'stevens.edu'), ('Matthew', 'github.com'),
            ('William', 'noob.com'), ('Lizzie', 'noob.com'),
        ]
        summary2 = [
            ('github.com', ['Matthew']),
            ('noob.com', ['Lizzie', 'William']), # my two 10 year old cousins
            ('stevens.edu', ['Matthew']),
        ]
        self.assertEqual(web_analyzer(weblogs1), summary1) 
        self.assertEqual(web_analyzer(weblogs2), summary2) 

web_analyzer_test = TestWebAnalyzer()
web_analyzer_test.test_web_analyzer()