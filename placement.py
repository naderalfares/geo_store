import sys
import json
import argparse
from argparse import ArgumentParser
from factory import obj_factory, json_to_obj
from cls import Group, DataCenter
from constants.opt_consts import PLACEMENT_CLASS_MAPPER, DATACENTER, GROUP

def parse_args():
    parser = ArgumentParser(description = 'Process cmd args for placements')
    parser.add_argument('-f','--file-name', dest='file_name', required=True)
    parser.add_argument('-p','--file-path', dest='file_path', default='',\
                        required=False)
    parser.add_argument('-t','--protocol', dest='protocol', required=True)
    #Passing no heuristic arg would result a brute force
    parser.add_argument('-H','--heuristic', dest='heuristic', default='brute_force',\
                        required=False)
    parser.add_argument('-v','--verbose', dest='verbose', action='store_true',\
                        required=False)
    args = parser.parse_args()
    return args

def process_input(file_name):
    datacenters = []
    groups = []
    with open(file_name, "r", encoding="utf-8-sig") as f:
        data = json.load(f)
    for dc in data.get("datacenters"):
        dc_obj = json_to_obj(dc, DATACENTER)
        datacenters.append(dc_obj)
    for grp in data.get("input_groups"):
        grp_obj = json_to_obj(grp, GROUP)
        groups.append(grp_obj)
    return datacenters, groups

def process_output(placement_obj, fname, verbose=False):
    if verbose:
        placement_obj.show()
    with open(fname, "w") as f:
        f.write(json.dumps(placement_obj.__dict__,\
                           sort_keys=True, indent=2))

def main():
    args = parse_args()
    file_name = args.file_path + '/' + args.file_name \
                    if args.file_path else args.file_name
    datacenters, groups = process_input(file_name)
    kwargs = { 'file_name': file_name,\
               'heuristic': args.heuristic,\
               'datacenters': datacenters,\
               'groups': groups }
    placement_cls = PLACEMENT_CLASS_MAPPER[args.protocol]
    placement_obj = obj_factory(placement_cls, **kwargs)
    placement_obj.find_placement()
    #out_file = './out/out_' + args.file_name.split('/')[-1]
    #process_output(placement_obj, out_file, args.verbose)

if __name__ == "__main__":
    main()
