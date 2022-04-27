import matplotlib
import matplotlib.pyplot as plt
import csv


def choosefile(i):
    return {
        0: '/home/spotoczek/PycharmProjects/AGH-MPR/lab1/results/results_send_recv_1node.csv',
        1: '/home/spotoczek/PycharmProjects/AGH-MPR/lab1/results/results_send_recv_2nodes.csv',
        2: '/home/spotoczek/PycharmProjects/AGH-MPR/lab1/results/results_ssend_recv_1node.csv',
        3: '/home/spotoczek/PycharmProjects/AGH-MPR/lab1/results/results_ssend_recv_2nodes.csv'
    }[i]


def choosePlotName(i):
    return {
        0: "Przepustowność (send, 1 node)",
        1: "Przepustowność (send, 2 nodes)",
        2: "Przepustowność (ssend, 1 node)",
        3: "Przepustowność (ssend, 2 nodes)",
    }[i]


for i in range(4):
    datafile = choosefile(i)

    with open(datafile) as file:
        lines = file.readlines()
        file.close()

    x = []
    y = []

    for line in lines:
        line = line.replace('\n', '')
        line = line.split(',')
        x.append(int(line[0]))
        y.append(float(line[1]))

    print("file: " + datafile)
    plt.plot(x, y, 'b.')
    plt.xlabel("Długość komunikatu [B]")
    plt.ylabel("Przepustowność [Mbit/s]")
    plt.title(choosePlotName(i))
    plt.grid()
    plt.autoscale()
    plt.show()
