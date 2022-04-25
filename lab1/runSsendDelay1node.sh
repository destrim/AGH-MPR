rm results_ssend_delay_1node.csv
for i in {1..1000}
do
    a=$(( 100*i ))
    mpiexec -machinefile ./1node -np 2 ./ssend_delay.py $a >> results_ssend_delay_1node.csv
done