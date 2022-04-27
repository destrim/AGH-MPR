import matplotlib.pyplot as plt


def chooseFile(i):
    return {
        0: '/home/spotoczek/PycharmProjects/AGH-MPR/lab2/res_small.csv',
        1: '/home/spotoczek/PycharmProjects/AGH-MPR/lab2/res_medium.csv',
        # 2: '/home/spotoczek/PycharmProjects/AGH-MPR/lab2/res_big.csv',
    }[i]


def choosePlotStyle(i):
    return {
        0: 'r.',
        1: 'g.',
        # 2: 'b.'
    }[i]


for i in range(2):
    datafile = chooseFile(i)

    with open(datafile) as file:
        lines = file.readlines()
        file.close()

    x = []
    y = []
    data = [[] for i in range(12)]

    for line in lines:
        line = line.replace('\n', '')
        line = line.split(';')
        data[int(line[0]) - 1].append(float(line[1]))

    for n in range(12):
        x.append(n + 1)
        y.append(sum(data[n]) / len(data[n]))

    print("file: " + datafile)
    plt.plot(x, y, choosePlotStyle(i))

plt.xlabel("Liczba procesorów")
plt.ylabel("Czas")
plt.title("Czas wykonania w zależności od liczby procesorów")
plt.grid()
plt.autoscale()
plt.show()
