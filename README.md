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


Configs
=======

```
usage: run.py [-h] [-c CONFIG] [-i INFILE] [-o OUTFILE] [-lf LOGFILE]
              [-nl NLAYERS] [-dfu DROPOUT_FRACTION_RU]
              [-dfw DROPOUT_FRACTION_RW] [-ld LAYERDIM [LAYERDIM ...]]
              [-opt OPTIMIZER] [-lr LEARNRATE] [-m MOMENTUM] [-trp TRAINPCT]
              [-em ERRMETRIC] [-a [APPEND]] [-e EPOCH]

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        input config JSON file
  -i INFILE, --infile INFILE
                        input file (csv)
  -o OUTFILE, --outfile OUTFILE
                        output file
  -lf LOGFILE, --logfile LOGFILE
                        log file to store the training time & RMSE value
  -nl NLAYERS, --nlayers NLAYERS
                        number of layers
  -dfu DROPOUT_FRACTION_RU, --dropout_fraction_ru DROPOUT_FRACTION_RU
                        fraction of R_Units to be dropped [0.0, 1.0)
  -dfw DROPOUT_FRACTION_RW, --dropout_fraction_rw DROPOUT_FRACTION_RW
                        fraction of input units to be dropped [0.0, 1.0)
  -ld LAYERDIM [LAYERDIM ...], --layerdim LAYERDIM [LAYERDIM ...]
                        layer dimensions
  -opt OPTIMIZER, --optimizer OPTIMIZER
                        name of the optimizer
  -lr LEARNRATE, --learnrate LEARNRATE
                        the learning rate
  -m MOMENTUM, --momentum MOMENTUM
                        the momentum
  -trp TRAINPCT, --trainpct TRAINPCT
                        training percent (0.0, 1.0]
  -em ERRMETRIC, --errmetric ERRMETRIC
                        type of error metric
  -a [APPEND], --append [APPEND]
                        append run configuration to logfile
  -e EPOCH, --epoch EPOCH
                        number of epochs to run

```
