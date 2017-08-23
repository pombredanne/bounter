import bounded_counter
from timeit import default_timer as timer
import cProfile

# You can use this to profile logcounter implementation
def test():
    expected = 1000000
    mks = bounded_counter.CountMinSketch(1, 1, 'logcounter1024')

    start = timer()
    for i in range(expected):
        mks.increment(1)
    end = timer()

    actual = mks[1]
    print("Got %d (%f of original %d)" % (actual, actual / expected, expected))
    log_actual = mks.log_encode(int(actual))
    log_expected = mks.log_encode(int(expected))
    print("Counter difference: %d (expected %d, actual %d)" % (log_actual - log_expected, log_expected, log_actual))
    print(mks.table[0,0])

    print("Time: %s" %(end - start))

cProfile.run('test()')

