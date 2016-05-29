# -*- coding: utf-8 -*- 
import numpy as np
import cv2
import sys
import commands

if __name__ == "__main__":
    
    if (len(sys.argv) != 2):
        print "usage: %s <image folder path>" % sys.argv[0]
        sys.exit()

    files = commands.getoutput("find %s -name \"*.png\"" % sys.argv[1]).split("\n")
    for i in files:
        print i
        image = cv2.imread(i)
        flipimage = cv2.flip(image, 1)
        cv2.imwrite(i.replace(".png", "_flipV.png"), flipimage)

