from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import facetrakcer
import os

IMAGES_BASE = 'images'

def savefig(title):
    plt.savefig(os.path.join(IMAGES_BASE, title), bbox_inches='tight', pad_inches=0)


def tutorial1():
    pass


if __name__ == '__main__':
    tutorial1()    
    plt.show()