from threading import Thread

from traffmon import peru_analyzer


THREAD_COUNT = 3


def get_chunks(l, n):
    """Yield n number of striped chunks from l."""
    for i in range(0, n):
        yield l[i::n]


def worker(time_chunks):
    for timestamp in time_chunks:
        print("FIXING %s" %timestamp)
        try:
            peru_analyzer(timestamp)
        except:
            print("ERROR: FAILED TO FIX %s" % timestamp)


def filler(time_end, time_start):
    time_start = int(time_start)
    time_end = int(time_end)

    timestamps = [a for a in range(time_start, time_end + 300, 300)]

    chunky = list(get_chunks(timestamps,THREAD_COUNT))

    threads = []

    for chunks in chunky:
        t = Thread(target=worker, args=(chunks,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == '__main__':
    import sys
    import time
    
    if (sys.argv[1:]):
        start = time.time()
    
        filler(*sys.argv[1:])

        print("TOTAL TIME USED TO FIX THIS: %s" % (time.time() - start))
    else:
        print("Usage: filler.py <time_end> <time_start>")
        print(" time_end: timestamp start in seconds, multiple of 5 mins")
        print(" time_start: timestamp end in seconds, multiple of 5 mins")

        print()

        print("Runs traffmon.py for all the nfsen records between ")
        print("<time_end> and <time_start> (included) in order to fill events in the past,")
        print("or correct mistakes")
