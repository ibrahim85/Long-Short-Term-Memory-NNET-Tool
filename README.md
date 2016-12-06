Command to run GUI
========================
```
python gui.py
```


Command to run CLI
========================
```
python run.py --infile <input filename> --outfile <output filename> --learnrate <(0.0,1.0]>
```
Other command-line options are given below.

Command-line options
====================
- Specify a config JSON file as input.
 * --config
- Specify input filename (.csv) -- \*required.
 * --infile
- Specify output filename -- \*required.
 * --outfile
- Specify log filename.
 * --logfile
- Specify the number of layers in the neural network.
 * --nlayers
- Specify the dimensions of each layer in the neural network.
 * --layerdim
- Specify the learning rate -- \*required.
 * --learnrate
- Specify the fraction of RUnits that are dropped out (value is in range [0.0, 1.0).
 * --dropout\_fraction\_ru
- Specify the fraction of input units that are dropped out (value is in range [0.0, 1.0).
 * --dropout\_fraction\_rw
- Specify the optimizer.
 * --optimizer
- Specify the momentum.
 * --momentum
- Specify the training percent (The value is in range (0.0, 1.0]).
 * --trainpct
- Specify the error metric.
 * --errmetric
- Specify the number of epochs.
 * --epoch 
- Append the run configuration to the logfile.
 * --append
- 
