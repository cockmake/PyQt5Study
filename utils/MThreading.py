import threading
import cv2 as cv
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