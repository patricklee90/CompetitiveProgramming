import tracemalloc,time,datetime

class Runtime:
    def __init__(self):
        self.beginTime = datetime.datetime.now()
        self.tracemalloc = tracemalloc.start()

    def stop(self):
        current, peak = tracemalloc.get_traced_memory()
        print(datetime.datetime.now() - self.beginTime)
        print(f'Current memory usage is {"{:.3f}".format(current / 10**6)}MB; Peak was {"{:.3f}".format(peak / 10**6)}MB')
        tracemalloc.stop()

