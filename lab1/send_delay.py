#!/usr/bin/env python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

max = 100000
msg = "S"


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

    output = "{delay} ms".format(delay=avg_res)

    print(output)
