import time
import resource


def run_method_under_test(methodToRun, input):
    time_start = time.perf_counter()
    result = methodToRun(input)
    time_elapsed = time.perf_counter() - time_start
    mem_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print(f"{time_elapsed:5.1f} secs {mem_mb:5.1f} MByte")
    return result
