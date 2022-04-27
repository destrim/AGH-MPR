#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 12
#SBATCH --sockets-per-node=2
#SBATCH --time=00:03:00
#SBATCH --partition=plgrid-short
#SBATCH --account=plgmpr22

size=300000000

module add plgrid/tools/openmpi
module add plgrid/libs/python-mpi4py/3.0.0-python-2.7

mpiexec -np 12 ./approx_pi.py $size >> res_big_problem.csv
