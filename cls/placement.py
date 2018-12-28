from services import placement_service
from constants import opt_consts as CONSTS

class PlacementBase:
    def __init__(self, **kwargs):
        self.file = kwargs['file_name']
        self.heurisitic = kwargs['heuristic'] if kwargs['heuristic'] \
                                              else CONSTS.BRUTE

    def init(self):
        with open(self.file, "r") as f:
            pass
            #fill the obj with json data

    def find_placement(self, heuristic):
        pass

class PlacementAbd(PlacementBase):
    def __init__(self, **kwargs):
        super(PlacementAbd, self).__init__(**kwargs)
        self.protocol = CONSTS.ABD

class PlacementCas(PlacementBase):
    def __init__(self, **kwargs):
        super(PlacementAbd, self).__init__(**kwargs)
        self.protocol = CONSTS.CAS


