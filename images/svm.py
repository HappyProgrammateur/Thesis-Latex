#!/usr/bin/env python
# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
from random import randrange

def foo():
    x = randrange(-50, 50)
    y = randrange(-50, 50)
    return (x**2, y**2, x * y)
    return (x**2, y**2, np.sqrt(2) * x * y)

def bar():
    x = randrange(-50, 50)
    y = randrange(-50, 50)
    return (x, y)

def highdim():
    fig = plt.figure()
    data = tuple(
            bar() for i in range(int(1e3/2))
           )
    data = np.array(data)
    idx = np.sum(data[:, :2]**2, 1) > 28**2
    idx = idx & (np.sum(data[:, :2]**2, 1) < 32**2)
    data = data[~idx]
    idx = np.sum(data[:, :2]**2, 1) < 30**2
    data1 = data[idx]
    data2 = data[~idx]
    plt.plot(data2[:, 0], data2[:, 1], 'bo')
    plt.plot(data1[:, 0], data1[:, 1], 'g+')
    c = plt.Circle((0, 0), 30, fill=False)
    plt.gca().add_artist(c)
    plt.savefig('svm_2d.png')

    #data1[:, 2] = np.random.randint(0, 8, data1.shape[0])
    #data2[:, 2] = np.random.randint(12, 20, data2.shape[0])
    data = tuple(
            foo() for i in range(int(1e3/2))
           )
    data = np.array(data)
    idx = np.sum(data[:, :2], 1) > 28**2
    idx = idx & (np.sum(data[:, :2], 1) < 32**2)
    data = data[~idx]
    idx = np.sum(data[:, :2], 1) < 30**2
    data1 = data[idx]
    data2 = data[~idx]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data1[:, 0], data1[:, 1], data1[:, 2], marker='+', c='g')
    ax.scatter(data2[:, 0], data2[:, 1], data2[:, 2], marker='o', c='b')
    #p = plt.Rectangle((0, 0), 100**2, 100**2, fill=False)
    #ax.add_patch(p)
    #art3d.pathpatch_2d_to_3d(p, z=15**2)
    ax.view_init(200, 135)
    plt.savefig('svm_3d.png')


def maxmarg():
    fig = plt.figure()
    data = tuple((randrange(0, 100), randrange(0, 100)) for i in range(int(1e3/2)))
    data = np.array(data)

    idx = data[:, 0] < 30
    idx |= data[:, 0] > 40
    data = data[idx, :]
    idx = data[:, 0] < 30
    data1 = data[idx, :]
    data2 = data[~idx, :]

    plt.plot(data1[:, 0], data1[:, 1], 'g+')
    plt.plot(data2[:, 0], data2[:, 1], 'bo')
    plt.plot((32, 32), (0, 100), 'k-')
    plt.plot((30, 40), (0, 100), 'k-')
    plt.plot((40, 30), (0, 100), 'k-')
    plt.plot((38, 38), (0, 100), 'k-')
    plt.savefig('svm_lin.png')

    fig = plt.figure()
    plt.plot(data1[:, 0], data1[:, 1], 'g+')
    plt.plot(data2[:, 0], data2[:, 1], 'bo')
    plt.plot((35, 35), (0, 100), 'k-')
    plt.savefig('svm_lin_maxmarg.png')


maxmarg()
highdim()
plt.show()
