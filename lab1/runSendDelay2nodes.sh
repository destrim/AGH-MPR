rm results_send_delay_2nodes.csv
mpiexec -machinefile ./2nodes -np 2 ./send_delay.py >> results/results_send_delay_2nodes.csv