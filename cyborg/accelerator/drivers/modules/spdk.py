"""
Cyborg SPDK driver modules implementation.
"""

from cyborg.accelerator.commom import exception
from cyborg.accelerator.drivers import base
from oslo_log import lof as logging
from oslo_config import cfg
from oslo_concurrency import processutils as putils

LOG = logging.getLogger(__name__)

libtype_opt = cfg.ListOpt('libtype',
                          defalut=['local', 'nvmf', 'iscsi', 'vhost'],
                          help=_('List of libtype to enable by default'))

rpc_opts = [
    cfg.BoolOpt('Enable',
                default=False,
                help=_('Default is disabled')),

    cfg.StrOpt('bind_host',
               defalut='127.0.0.1',
               help=_('Listen 127.0.0.1'))
]

malloc_opts = [
    cfg.IntOpt('NumberOfLuns',
                default=8,
                help=_('Malloc Luns')),

    cfg.IntOpt('LunSizeInMB',
                efalut=64,
                help=_('Each LUN will be size 64MB'))
]

nvme_opts = [
    cfg.ListOpt('TransportId',
                default=['trtype:PCIe traddr:0000:00:00.0',
                         'trtype:PCIe traddr:0000:01:00.0']),

    cfg.ListOpt('NvmeName',
                default=['Nvme0', 'Nvme1']),

    cfg.IntOpt('AdminPollRate',
                default=100000,
                help=_('Units in microseconds'))
]

CONF = cfg.CONF
CONF.register_opt(libtype_opt)
CONF.register_opts(rpc_opts)
CONF.register_opts(malloc_opts)
CONF.register_opts(nvme_opts)

print(CONF.Nv)
class SPDKDRIVER(base.BaseDriver):

    def __init__(self, execute=putils.execute, *args, **kwargs):
        super(SPDKDRIVER, self).__init__(execute, *args, **kwargs)

    def install_driver(self, driver_type):
        self.check_driver(driver_type)
        ctrlr = self.get_controller()
        nsid = self.get_allocated_nsid(ctrlr)
        self.attach_instance(nsid)
        pass

    def uninstall_driver(self, driver_type):
        self.check_driver(driver_type)
        ctrlr = self.get_controller()
        nsid = self.get_allocated_nsid(ctrlr)
        self.detach_instance(nsid)
        pass

    def discover_driver(self, driver_type):
        pass

    def driver_list(self, driver_type):
        self.check_driver(driver_type)
        self.display_controller_list()

    def update(self, driver_type):
        self.check_driver(driver_type)
        pass

    def attach_instance(self, instance_id):
        self.add_ns()
        self.attach_and_detach_ns()
        pass

    def detach_instance(self, instance_id):
        self.delete_ns()
        self.detach_and_detach_ns()
        pass

    def get_controller(self):
        pass

    '''list controllers'''
    def display_controller_list(self):
        pass

    '''create namespace'''
    def add_ns(self):
        pass

    '''delete namespace'''
    def delete_ns(self):
        pass

    '''attach namespace to controller'''
    def attach_and_detach_ns(self):
        pass

    '''detach namespace from controller'''
    def detach_and_detach_ns(self):
        pass

    '''	format namespace or controller'''
    def format_nvm(self):
        pass

    def get_allocated_nsid(self, ctrl):
        return self.nsid

    def check_driver(self, driver_type):
        if driver_type is 'SPDK':
            return True
        else:
            return False

