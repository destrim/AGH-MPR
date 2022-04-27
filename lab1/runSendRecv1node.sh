rm results_send_recv_1node_16k.csv
for i in {1..160}
do
    a=$(( 100*i ))
    mpiexec -machinefile ./1node -np 2 ./send_recv.py $a >> results/results_send_recv_1node_16k.csv
done
