#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 12
#SBATCH --sockets-per-node=2
#SBATCH --time=00:10:00
#SBATCH --partition=plgrid-short
#SBATCH --account=plgmpr22

size=10000

module add plgrid/tools/openmpi
module add plgrid/libs/python-mpi4py/3.0.0-python-2.7

for i in {1..10}
do
    for th in {1..12}
    do
      mpiexec -np $th ./approx_pi.py $size >> res_small.csv
    done
done