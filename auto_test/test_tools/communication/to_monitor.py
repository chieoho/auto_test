
"""
requests to monitor
"""

from auto_test.test_tools.communication.poster import HttpPoster


class MonitorPoster(HttpPoster):
    """
    requests to Monitor
    """

    def __init__(self):
        super(MonitorPoster, self).__init__()

    def add_scan_path(self):
        pass
