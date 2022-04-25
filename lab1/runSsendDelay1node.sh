rm results_ssend_delay_1node.csv
mpiexec -machinefile ./1node -np 2 ./ssend_delay.py >> results_ssend_delay_1node.csv