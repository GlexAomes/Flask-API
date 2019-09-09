import queue

# delegate that will handle a queue in order to do
# message passing between threads
def call_tail_recursive_fib(n:int, q:queue):
    q.put(tail_recursive_fib(n))

# standard tail recursive fib
# max recursion depth x, 950 < x < 1000
def tail_recursive_fib(n:int, m:int=0, acc:int=1) -> int:
    if n == 0:
        return m
    if n == 1:
        return acc
    return tail_recursive_fib(n-1, acc, m + acc)