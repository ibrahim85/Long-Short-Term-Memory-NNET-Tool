#!usr/bin/python

import machine_learning_project
import sys

if __name__ == "__main__":
    if len(sys.argv) < 10:
        print("Usage: run.py <input filename> <number of layers> <number of drop out layers> [<layer dimensions>] <optimizer> <learning rate> <momentum> <err_metric> <output_filename>")
    else:
        args = sys.argv
	for arg in args:
		print arg
        err_metric = None
        if len(args) == 10 and args[7] != "":
            err_metric = args[8]
        machine_learning_project.run_nnet(args[1], int(args[2]), int(args[3]), list(map(int, args[4].split(","))), args[5], float(args[6]), float(args[7]), err_metric, args[9])
