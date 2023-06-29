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


import threading
class MThread(threading.Thread):
    def __init__(self, args=(), daemon=None):
        super(MThread, self).__init__(daemon=daemon)
        self.stop_flag = False
        self.args = args

    def run(self) -> None:
        # 重写这个函数被start调用, 可以使用传过来的一些参数
        try:
            cap = cv.VideoCapture(0)
        except Exception as E:
            print(E)
            # 未打开摄像头
            return
        try:
            while True:
                f, img = cap.read()
                if not f or self.stop_flag: break
                cv.imshow("1", img)
                q = cv.waitKey(1)
                if q == ord('q'): break
        except Exception as E:
            print(E)
        finally:
            if cap.isOpened(): cap.release()
            cv.destroyAllWindows()