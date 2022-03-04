import threading
#import thread
import queue
def threaded_func(a, b, q):
  #return a + b
  ret = a + b
  q.put(ret)
def main():
  q =queue.Queue()
  th = threading.Thread(target=threaded_func, args=(1, 2, q))
  th.start()
#  th.join()
  rslt = q.get()
  print(rslt)
if __name__ == '__main__':
  main()