from .tesla_pids import pids as tesla_pids
from .obd_pids import pids as obd_pids
from .csvrotator import CSVLogRotator
tesla_name2pid = {y['name']: x for x, y in tesla_pids.items()}
obd_name2pid = {y['name']: x for x, y in obd_pids.items()}
