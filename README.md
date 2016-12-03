Configs
=======

TODO:
 * Need to generate results by changing the learning rate
 * Need to generate results by changing the momentum
 * Need to generate results by changing the number of layers to dropout

```
usage: run.py [-h] -i INFILE -o OUTFILE [-lf LOGFILE] [-nl NLAYERS]
              [-ndl NDROPLAYERS] [-ld LAYERDIM [LAYERDIM ...]]
              [-opt OPTIMIZER] [-lr LEARNRATE] [-m MOMENTUM] [-trp TRAINPCT]
              [-em ERRMETRIC] [-a [APPEND]]

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        input file (csv)
  -o OUTFILE, --outfile OUTFILE
                        output file
  -lf LOGFILE, --logfile LOGFILE
                        log file to store the training time & RMSE value
  -nl NLAYERS, --nlayers NLAYERS
                        number of layers
  -ndl NDROPLAYERS, --ndroplayers NDROPLAYERS
                        number of dropout layers
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
