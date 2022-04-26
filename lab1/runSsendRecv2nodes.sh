rm results_ssend_recv_2nodes.csv
for i in {1..160}
do
    a=$(( 100*i ))
    mpiexec -machinefile ./2nodes -np 2 ./ssend_recv.py $a >> results_ssend_recv_2nodes.csv
done
