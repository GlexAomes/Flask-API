import timeit as tmr
import queue

import threading

from fib import *

# Rough tasking delegator that will make a threaded call to a fib function
# and pull its return result from the passed queue which will be handled
# by the fib function's internal delegator.
# The result and the time of execution is stored within the class's property
# and accessed by API as such.
class Tasker:
    TIME = None
    RESPONSE = None

    def fib(self, n:int):
        print('Starting fib task...')

        t_start = tmr.default_timer()

        thread_queue = queue.Queue()
        thread = threading.Thread(target=call_tail_recursive_fib(n, thread_queue))
        thread.daemon = True
        thread.start()
        thread.join()

        result = thread_queue.get()

        t_end = tmr.default_timer()

        elapsed = '{0:.3f}ms'.format(round((t_end - t_start) * 1000, 3))
        self.TIME = elapsed

        print(f'Completed fib task in {elapsed}')

        self.RESPONSE = result