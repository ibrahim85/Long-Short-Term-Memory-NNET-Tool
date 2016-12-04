Configs
=======

```
usage: run.py [-h] [-c CONFIG] [-i INFILE] [-o OUTFILE] [-lf LOGFILE]
              [-nl NLAYERS] [-dfu DROPOUT_FRACTION_U]
              [-dfW DROPOUT_FRACTION_W] [-ld LAYERDIM [LAYERDIM ...]]
              [-opt OPTIMIZER] [-lr LEARNRATE] [-m MOMENTUM] [-trp TRAINPCT]
              [-em ERRMETRIC] [-a [APPEND]]

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
  -dfu DROPOUT_FRACTION_U, --dropout_fraction_U DROPOUT_FRACTION_U
                        fraction of R_Units to be dropped [0.0, 1.0)
  -dfW DROPOUT_FRACTION_W, --dropout_fraction_W DROPOUT_FRACTION_W
                        fraction of input units to be dropped [0.0, 1.0)
			If this is given (and is not 0) then this will be chosen instead of DROPUT_FRACTION_U
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
```

TODO:

 * Need to generate results by changing the number of layers to dropout
 * We need to set up cross validation for all selected models.
 * Run ARIMA and HMM to show that the machine learning model is better than the statistical models.
