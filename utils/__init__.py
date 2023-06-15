import cv2 as cv
from PyQt5.QtGui import QImage
def cvimg_to_qtimg(cvimg):
    height, width, depth = cvimg.shape
    cvimg = cv.cvtColor(cvimg, cv.COLOR_BGR2RGB)
    cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)
    return cvimg