rm results_send_recv_1node.csv
for i in {1..1000}
do
    a=$(( 100*i ))
    mpiexec -machinefile ./1node -np 2 ./send_recv.py $a >> results_send_recv_1node.csv
done