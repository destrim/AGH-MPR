rm results_ssend_recv_1node.csv
for i in {1..160}
do
    a=$(( 100*i ))
    mpiexec -machinefile ./1node -np 2 ./ssend_recv.py $a >> results_ssend_recv_1node.csv
done
