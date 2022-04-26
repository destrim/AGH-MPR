rm results_pi.csv
for i in {1..12}
do
  mpiexec -machinefile nodes -np $i ./approx_pi.py 1000000 >> results_pi.csv
done