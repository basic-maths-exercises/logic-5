import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_noutside(self):
        n=0
        for d in data : 
           if d<3 or d>7 : n = n + 1
        self.assertTrue( numberOutside( data, 3, 7)==n, "Your function for determining the number outside is not working" )
        n=0
        for d in data : 
           if d<2 or d>5 : n = n + 1
        self.assertTrue( numberOutside( data, 2, 5)==n, "Your function for determining the number outside is not working" )
        n=0
        for d in data : 
           if d<6 or d>9 : n = n + 1 
        self.assertTrue( numberOutside( data, 6, 9)==n, "Your function for determining the number outside is not working" )
