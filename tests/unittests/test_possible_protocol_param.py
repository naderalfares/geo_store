import sys, unittest
sys.path.append('../../')
from utils import *



class TestPossibleProtocolParam(unittest.TestCase):
    def test_abd_possible_param(self):
        params = gen_abd_params(3,1)
        self.assertEqual(len(params) , 1)
        self.abd_params_are_valid(params)
        
        params = gen_abd_params(5,2)
        self.assertEqual(len(params) , 15)
        self.abd_params_are_valid(params)
    
    def test_cas_possible_param(self):
        params = gen_cas_params(3,1)
        self.assertEqual(len(params), 1)
        self.cas_param_is_valid(params)
    
    def cas_params_are_valid(self,parameters):
        for p in parameters:
            self.assertTrue(p[2] + p[4] > p[0])
            self.assertTrue(p[2] + p[5] > p[0])
            self.assertTrue(p[3] + p[5] >= p[0] + p[1])
            self.assertTrue(p[5] >= p[1])
        
    def abd_params_are_valid(self,parameters):
        for p in parameters:
            self.assertTrue(p[0] > p[1] +  p[2])

if __name__ == '__main__':
    unittest.main()    
