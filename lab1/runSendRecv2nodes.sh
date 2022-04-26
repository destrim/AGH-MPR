rm results_send_recv_2nodes.csv
for i in {1..160}
do
    a=$(( 100*i ))
    mpiexec -machinefile ./2nodes -np 2 ./send_recv.py $a >> results_send_recv_2nodes.csv
done
