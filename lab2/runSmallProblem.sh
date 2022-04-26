#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 12
#SBATCH --sockets-per-node=2
#SBATCH --time=00:01:00
#SBATCH --partition=plgrid-short
#SBATCH --account=plgmpr22

size=10000

module add plgrid/tools/openmpi
mpiexec -np 1 ./approx_pi.py $size >> res_small_problem.csv
