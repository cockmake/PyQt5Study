import cv2 as cv
from PyQt5.QtGui import QImage
import ctypes
import inspect
def async_raise(tid, exctype):
    try:
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            print("该线程已经被销毁")
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
    except Exception as E:
        print(E)
def stop_thread(thread):
    async_raise(thread.ident, None)
def cvimg_to_qtimg(cvimg):
    height, width, depth = cvimg.shape
    cvimg = cv.cvtColor(cvimg, cv.COLOR_BGR2RGB)
    cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)
    return cvimg

