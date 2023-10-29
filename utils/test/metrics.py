import time
import resource


def run_method_under_test(methodToRun, input):
    time_start = time.perf_counter()
    result = methodToRun(input)
    time_elapsed = time.perf_counter() - time_start
    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("%5.1f secs %5.1f MByte" % (time_elapsed, memMb))
    return result
