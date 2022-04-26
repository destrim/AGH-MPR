from random import random
from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

p_max = int(sys.argv[1])
in_circle = 0
p_per_node = int(p_max / size)

comm.Barrier()
time_start = MPI.Wtime()

for i in range(p_max):
    x = random()
    y = random()
    if (x * x + y * y) <= 1:
        in_circle += 1

total_in_circle = comm.reduce(in_circle, op=MPI.SUM, root=0)
if rank == 0:
    res = 4 * total_in_circle / p_max
    time_end = MPI.Wtime()
    time = time_end - time_start

    output = "{size};{time};{p_max}".format(size=size, time=time, p_max=p_max)
    print(output)
