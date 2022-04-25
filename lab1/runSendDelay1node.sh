rm results_send_delay_1node.csv
mpiexec -machinefile ./1node -np 2 ./send_delay.py >> results_send_delay_1node.csv