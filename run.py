from Attop import Attop
from multiprocessing import Process

if __name__ == '__main__':
    app = Attop()
    p = Process(target=app.watch)
    q = Process(target=app.comment)
    p.start()
    q.start()
    p.join()
    q.join()
    print('- all done')
