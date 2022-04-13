import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from chirplet import gaussian_chirplet, estimate_gaussian_chirplet_parameters

import numpy as np

class TestCode():

    def __init__(self):
        self.y = 0
        self.y0 = 0
        self.t = 0

    def test1_chirplet(self):
        """
        """
        import matplotlib.pyplot as plt

        y0 = np.genfromtxt('data1.csv', delimiter=',')
        y0 = y0[0,:] + 1j*y0[1,:]

        t = np.linspace(-3, 3, len(y0))
        y = gaussian_chirplet(t)

        fig, ax = plt.subplots(1,2, sharex=False)

        ax[0].plot(t,y0.real,label='y0')
        ax[0].plot(t,y.real,label='y')
        ax[0].grid()
        ax[0].legend()
        ax[0].set_title('real')

        ax[1].plot(t,y0.imag,label='y0')
        ax[1].plot(t,y.imag,label='y')
        ax[1].grid()
        ax[1].legend()
        ax[1].set_title('imag')

        plt.show()

        parameters = estimate_gaussian_chirplet_parameters(y0, t)
        print(parameters)
        y = gaussian_chirplet(t, *parameters.values())

        fig, ax = plt.subplots(1,2, sharex=False)

        ax[0].plot(t,y0.real,label='y0')
        ax[0].plot(t,y.real,label='y')
        ax[0].grid()
        ax[0].legend()
        ax[0].set_title('real')

        ax[1].plot(t,y0.imag,label='y0')
        ax[1].plot(t,y.imag,label='y')
        ax[1].grid()
        ax[1].legend()
        ax[1].set_title('imag')

        plt.show()


if __name__ == '__main__':
    print('Running unit tests for chirplet')
    TC = TestCode()
    TC.test1_chirplet()
