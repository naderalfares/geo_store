import sys, unittest
import json


class TestPlacements(unittest.TestCase):
    config = None
    
    def setUp(self):
        self.assertTrue(config is not None)
    def test_qourm_sizes(self):
        
        #XXX: this can be replaced by an input object
        expected_results   = TestPlacements.config["expected_results"]        
        
        expected_protocol           = expected_results["protocol"]
        expected_placement = expected_results["dc_ids"]
        expected_n         = len(expected_placements)
        expected_q1        = expected_results["Q1"]
        expected_q2        = expected_resutls["Q2"]
        if protocol is "CAS":
            expected_q3    = expected_results["Q3"]
            expected_q4    = expected_results["Q4"]
        
        #TODO: retrive data from output file
        #XXX:  This can be replaced by an input object
        protocol = "ABD"
        n = 0
        placement = []
        q1 = 0
        q2 = 0
        # if output protocol is cas, assign the following
        q3 = 0
        q4 = 0
        #######
        self.assertTrue(expected_protocol == protcol)
        self.assertTrue(expected_n == n)
        self.assertTrue(expected_placement == placement)
        self.assertTrue(expected_q1 == q1)
        self.assertTrue(expected_q2 == q2)
        ## only check if expected protocol == output protocol
        self.assertTrue(expected_q3 == q3)
        self.assertTrue(expected_q4 == q4)

if __name__ =  "__main__":
    args = sys.argv
    if len(sys.argv) < 2:
        print("USAGE: python3 test_placements.py <conifg.json>")
        sys.exit(0)
    try:
        TestPlacements.config = json.load(open(args[2], 'r'))
    except:
        print("FILE ERROR")

    






    
