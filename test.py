import unittest
def add(a,b):
    return a+b
class Add(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10,15),25)
if __name__=="__main__":
    unittest.main()        
