import matplotlib.pyplot as plt

datafile = '/home/spotoczek/PycharmProjects/AGH-MPR/lab2/results_pi.csv'

x = []
y = []

with open(datafile) as file:
    lines = file.readlines()
    file.close()

for line in lines:
    line = line.replace('\n', '')
    line = line.split(';')
    x.append(int(line[0]))
    y.append(float(line[1]))

print("file: " + datafile)
plt.plot(x, y, 'r.')

plt.xlabel("Liczba procesorów")
plt.ylabel("Czas [s]")
plt.title("Czas wykonania w zależności od liczby procesorów - vcluster")
plt.grid()
plt.autoscale()
plt.show()
