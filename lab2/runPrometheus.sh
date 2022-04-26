#!/bin/bash -l
#SBATCH --nodes 1
#SBATCH --ntasks 12
#SBATCH --sockets-per-node=2
#SBATCH --time=02:00:00
#SBATCH --partition=plgrid
#SBATCH --account=plgmpr22

size=10000,10000000,100000000

module add plgrid/tools/openmpi

for s in ${size//,/ }
do
  for i in {1..15}
  do
      for th in {1..12}
      do
        mpiexec -np $th ./approx_pi.py $s
      done
  done
done