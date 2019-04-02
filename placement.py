import sys
import json
import argparse
from argparse import ArgumentParser
from factory import obj_factory, json_to_obj
from cls import Group, DataCenter
from constants.opt_consts import PLACEMENT_CLASS_MAPPER, DATACENTER, GROUP,\
        CAS, ABD, CAS_K_1, PLACEMENT_BASE

def parse_args():
    parser = ArgumentParser(description = 'Process cmd args for placements')
    parser.add_argument('-f','--file-name', dest='file_name', required=True)
    parser.add_argument('-o','--out-file', dest='outfile', required=False)
    parser.add_argument('-p','--file-path', dest='file_path', default='',\
                        required=False)
    parser.add_argument('-t','--protocol', dest='protocol', required=False)
    parser.add_argument('-k','--k', dest='k', required=False)
    parser.add_argument('-m','--m', dest='m', required=False)
    #Passing no heuristic arg would result a brute force
    parser.add_argument('-H','--heuristic', dest='heuristic', default='brute_force',\
                        required=False)
    parser.add_argument('-b','--baseline', dest='baseline', action='store_true',\
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

def baseline(args, datacenters, groups):
    out_file = args.outfile
    if out_file is None:
        out_file = './out/out_'+args.protocol+'_baseline_'+args.file_name.split('/')[-1]
    kwargs = {  'heuristic': args.heuristic,\
                'file_name': out_file,\
                'k': args.k,\
                'm': args.m,\
                'verbose': args.verbose,\
                'datacenters': datacenters,\
                'groups': groups }
    if args.protocol is None:
        print("Protocol cannot be None")
        return
    placement_cls = PLACEMENT_CLASS_MAPPER[args.protocol]
    placement_obj = obj_factory(placement_cls, **kwargs)
    placement_obj.find_placement()
    placement_obj.write_output()

def main(args, datacenters, groups):
    out_file = args.outfile
    if out_file is None:
        out_file = './out/out_'+args.protocol+'_baseline_'+args.file_name.split('/')[-1]
    kwargs = {  'file_name': out_file,\
                'heuristic': args.heuristic,\
                'k': None,\
                'm': None,\
                'verbose': args.verbose,\
                'datacenters': datacenters,\
                'groups': groups }
    placement_obj = obj_factory(PLACEMENT_BASE, **kwargs)
    placement_obj.find_placement()
    placement_obj.write_output()


if __name__ == "__main__":
    args = parse_args()
    file_name = args.file_path + '/' + args.file_name \
                    if args.file_path else args.file_name
    datacenters, groups = process_input(file_name)
    if args.baseline is True:
        baseline(args, datacenters, groups)
    else:
        main(args, datacenters, groups)
