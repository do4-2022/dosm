import sys
import threading


def parallel_run(fct, callback, *args):
    """
    Run `fct` with `args` arguments in another thread.
    Call `callback` when the operation is finished.

    Returns the thread which has just been started.
    """
    def run_in_thread():
        callback(fct(*args))

    thread = threading.Thread(target=run_in_thread)
    thread.start()

    return thread


def parse_int_sort(t):
    """
    Try to parse string stored as first item of `t` as an integer.
    If this string does not represent an integer return float('inf').
    """
    if isinstance(t[0], str) and t[0].isdigit():
        return int(t[0])
    return float('inf')