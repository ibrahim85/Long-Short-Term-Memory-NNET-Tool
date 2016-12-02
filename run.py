#!usr/bin/python

import machine_learning_project
import sys

if __name__ == "__main__":
    if len(sys.argv) < 7:
        print("Usage: run.py <input filename> <number of layers> <number of drop out layers> <optimizer> <learning rate> <momentum> <err_metric> <output_filename>")
    else:
        args = sys.argv
        err_metric = None
        if len(args) == 9 and args[7] != "":
            err_metric = args[7]
        machine_learning_project.run_nnet(args[1], int(args[2]), int(args[3]), args[4], float(args[5]), float(args[6]), err_metric, args[8])
