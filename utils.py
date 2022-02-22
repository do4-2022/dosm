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