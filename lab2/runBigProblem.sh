#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 12
#SBATCH --sockets-per-node=2
#SBATCH --time=00:20:00
#SBATCH --partition=plgrid-short
#SBATCH --account=plgmpr22

module add plgrid/tools/openmpi
module add plgrid/libs/python-mpi4py/3.0.0-python-2.7

for i in {1..9}
do
  size=$((100000000 * i))
  mpiexec -np 12 ./approx_pi.py $size >> search_big.csv
done
