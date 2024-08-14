#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    ip_address = "{:d}.{:d}.{:d}.{:d}".format(
            random.randint(1, 255), random.randint(1, 255),
            random.randint(1, 255), random.randint(1, 255)
    )
    timestamp = datetime.datetime.now()
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    data_size = random.randint(1, 1024)

    sys.stdout.write(
        f"{ip_address} - [{timestamp}] \"GET /projects/260 HTTP/1.1\" "
        f"{status_code} {data_size}\n"
    )
    sys.stdout.flush()
