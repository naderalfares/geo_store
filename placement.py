import sys
#sys.path.append('/home/sobasu/research/geo_store')
import json
import argparse
from argparse import ArgumentParser
from utils import generate_placements, obj_factory
from constants.opt_consts import PLACEMENT_CLASS_MAPPER

def parse_args():
    parser = ArgumentParser(description = 'Process cmd args for placements')
    parser.add_argument('-f','--file-name', dest='file_name', required=True)
    parser.add_argument('-p','--file-path', dest='file_path', default='',\
                        required=False)
    parser.add_argument('-t','--protocol', dest='protocol', required=True)
    #Passing no heuristic arg would result a brute force
    parser.add_argument('-H','--heuristic', dest='heuristic', default='',\
                        required=False)
    parser.add_argument('-v','--verbose', dest='verbose', action='store_true',\
                        required=False)
    args = parser.parse_args()
    return args

def process_output(placement_obj, fname, verbose=False):
    if verbose:
        placement_obj.show()
    with open(fname, "w") as f:
        f.write(json.dumps(placement_obj.__dict__,\
                           sort_keys=True, indent=2))

def main():
    args = parse_args()
    file_name = args.file_path + '/' + args.file_name
    kwargs = {'file_name': file_name,\
              'heuristic': args.heuristic}
    _type = PLACEMENT_CLASS_MAPPER[args.protocol]
    placement_obj = obj_factory(_type, **kwargs)
    print(type(placement_obj))
    #placement_obj.find_placement()
    print(placement_obj.__dict__)
    out_file = './out/out_' + args.file_name.split("/")[-1]
    process_output(placement_obj, out_file, args.verbose)

if __name__ == "__main__":
    main()
