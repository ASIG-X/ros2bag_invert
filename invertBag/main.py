'''
    The main file for the ros2bag_invert script
'''
#!/usr/bin/env python3
import argparse
import os, sys
from pathlib import Path

from invert_bag import invert_bag

if __name__ == "__main__":
    # load input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', type=str)
    parser.add_argument('-dst', type=str)
    parser.add_argument('-msg_paths', type=str, nargs='+')
    args = parser.parse_args()
    print('Converting the following file from ROS2 to ROS:')
    print(args.src)

    src_path = [Path(args.src)]
    dst_path = Path(args.dst)
    msg_paths = args.msg_paths
    invert_bag(src_path, dst_path, msg_paths)
    print('Conversion completed!')
