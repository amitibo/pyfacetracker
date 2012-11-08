from __future__ import division
import numpy as np
import facetracker
from scipy.misc import lena
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import logging
import Image

IMG_PATH = './images6.jpg'


def main():
    #
    # Load image
    #
    img = Image.open(IMG_PATH)
    gray = img.convert('L')
    img = np.asanyarray(img)
    gray = np.asarray(gray)

    #
    # Load face model
    #
    conns = facetracker.LoadCon(r'..\model\face.con')
    trigs = facetracker.LoadTri(r'..\model\face.tri')
    tracker = facetracker.FaceTracker(r'..\model\face.tracker')
    
    #
    # Search for faces in the image
    #
    tracker.setWindowSizes((21, 19, 17, 15, 13, 11, 9, 7))
    print tracker.update(gray)
    print tracker.getPosition()
    print tracker.getScale()
    print tracker.getOrientation()
    print tracker.getShape()
    img = tracker.draw(img, conns, trigs)

    obj3D = tracker.getObjectShape()
    
    plt.figure()
    plt.imshow(img)
    
    fig3d = plt.figure()
    ax = fig3d.add_subplot(111, projection='3d')
    ax.scatter(obj3D[:66, 0], obj3D[66:132, 0], obj3D[132:, 0])
    for i in range(66):
        ax.text(obj3D[i], obj3D[i+66], obj3D[i+132], str(i))
    
    plt.show()
    
    
if __name__ == '__main__':
    main()
    