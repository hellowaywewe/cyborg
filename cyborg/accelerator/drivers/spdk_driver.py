"""
Cyborg SPDK driver implementation
"""

from modules import spdk

class SPDKDriver(object):
    def __init__(self):
        self.discover = spdk.discover()
        self.list = spdk.list()
        self.attach = spdk.attach()
        self.detach = spdk.detach()
        self.update = spdk.update()
