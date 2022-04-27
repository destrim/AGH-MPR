#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 12
#SBATCH --sockets-per-node=2
#SBATCH --time=00:20:00
#SBATCH --partition=plgrid-short
#SBATCH --account=plgmpr22

module add plgrid/tools/openmpi
module add plgrid/libs/python-mpi4py/3.0.0-python-2.7

mpiexec -np 12 ./approx_pi.py 100000000 >> res_big_problem.csv
mpiexec -np 12 ./approx_pi.py 200000000 >> res_big_problem.csv
mpiexec -np 12 ./approx_pi.py 300000000 >> res_big_problem.csv
mpiexec -np 12 ./approx_pi.py 400000000 >> res_big_problem.csv
mpiexec -np 12 ./approx_pi.py 500000000 >> res_big_problem.csv
mpiexec -np 12 ./approx_pi.py 600000000 >> res_big_problem.csv
mpiexec -np 12 ./approx_pi.py 700000000 >> res_big_problem.csv
mpiexec -np 12 ./approx_pi.py 800000000 >> res_big_problem.csv
mpiexec -np 12 ./approx_pi.py 900000000 >> res_big_problem.csv

