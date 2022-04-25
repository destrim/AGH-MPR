rm results_ssend_delay_2nodes.csv
mpiexec -machinefile ./2nodes -np 2 ./ssend_delay.py >> results_ssend_delay_2nodes.csv