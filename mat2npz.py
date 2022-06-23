# Access double arrays from .mat files as an npz file.

from numpy import savez_compressed
import scipy.io as sio
import sys


def mat2npz(filename):
    mat_contents = sio.loadmat(filename)
    narrayname = filename[:-4]
    narray = mat_contents[narrayname]
    savez_compressed(narrayname + ".npz", narray)


if __name__ == '__main__':
    filename = sys.argv[1]
    mat2npz(filename)
