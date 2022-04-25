rm results_ssend_delay_2nodes.csv
for i in {1..1000}
do
    a=$(( 100*i ))
    mpiexec -machinefile ./2nodes -np 2 ./ssend_delay.py $a >> results_ssend_delay_2nodes.csv
done