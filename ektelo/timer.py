
from time import time
from functools import wraps
import csv
import os 

def simple_time_tracker(log_fun):
    def _simple_time_tracker(fn):
        @wraps(fn)
        def wrapped_fn(*args, **kwargs):
            start_time = time()

            try:
                result = fn(*args, **kwargs)
            finally:
                elapsed_time = time() - start_time
                # log the result
                log_fun({
                    'function_name': '.'.join((fn.__module__, fn.__name__)),
                    'total_time': elapsed_time,
                    'Aname':os.environ['Aname'],
                    'domain':os.environ['domain'],
                    'trial': os.environ['trial'],
                })
                
            return result

        return wrapped_fn
    return _simple_time_tracker

def log_to_file(message):
    with open(os.environ['detail_file'], 'a') as f:
        writer = csv.writer(f)
        writer.writerow([
                    message['Aname'], 
                    message['domain'],
                    message['trial'],
                    message['function_name'],
                    message['total_time']])  
    print('[SimpleTimeTracker] {Aname} {domain} {trial} {function_name} {total_time:.3f}'.format(**message))

