from os import environ

'''
Specifies the maximum number of pending connections.
'''
backlog = 2048

'''
Specifies the number of worker processes for
handling requests.

Workers are forked webserver processes. If using
threads and workers together the concurrency of
the application would be max
`threads` * `workers`.
'''
workers = environ.get('WEB_CONCURRENCY', 1)
worker_class = 'sync'
worker_connections = 1000

'''
Load application code before the worker processes
are forked.

By preloading an application you can save some
RAM resources as well as speed up server boot
times. Although, if you defer application
loading to each worker process, you can reload
your application code easily by restarting workers.
'''
preload_app = True
