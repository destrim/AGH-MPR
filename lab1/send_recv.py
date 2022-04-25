#!/usr/bin/env python
from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

max = 10000
num_of_bytes = int(sys.argv[1])
msg = "S" * num_of_bytes


def pingpong():
    comm.Barrier()
    t0 = MPI.Wtime()

    if rank == 0:
        comm.send(msg, dest=1)
        comm.recv(source=1)
    elif rank == 1:
        received_msg = comm.recv(source=0)
        comm.send(received_msg, dest=0)

    t1 = MPI.Wtime()

    return t1 - t0


t_sum = 0

for n in range(max):
    t = pingpong()
    t_sum = t_sum + t

if rank == 0:
    avg_res = t_sum / max
    megabits_per_sec = num_of_bytes * 8 / avg_res / 1_000_000

    output = "{bytes},{speed}".format(bytes=num_of_bytes, speed=megabits_per_sec)

    print(output)
