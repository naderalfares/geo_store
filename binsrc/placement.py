import sys
import argparse
from argparse import ArgumentParser
from utils import generate_placements
from cls.placement import Placement

def parse_args():
    """ Process command line arguments
    """
    parser = ArgumentParser(description = 'Process cmd args for placements')
    parser.add_argument('-f','--file-name', dest='file_name', required=True)
    parser.add_argument('-p','--file-path', dest='file_path', required=False)
    parser.add_argument('-t','--protocol', dest='protocol', required=True)
    parser.add_argument('-h','--heuristic', dest='heuristic', required=False)
    #parser.add_argument('-b','--brute-force', dest='brute_force', action='store_true', required=False)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()


