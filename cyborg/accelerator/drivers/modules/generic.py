# Copyright 2017 Lenovo, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""
Cyborg Generic driver modules implementation.
"""

from cyborg.accelerator.common import exception
from cyborg.accelerator.drivers import base
from oslo_log import log as logging
from oslo_concurrency import processutils as putils

LOG = logging.getLogger(__name__)

# TODO(crushil): REQUIRED_PROPERTIES needs to be filled out.
REQUIRED_PROPERTIES = {}
COMMON_PROPERTIES = REQUIRED_PROPERTIES


def _check_for_missing_params(info_dict, error_msg, param_prefix=''):
    missing_info = []
    for label, value in info_dict.items():
        if not value:
            missing_info.append(param_prefix + label)

    if missing_info:
        exc_msg = _("%(error_msg)s. Missing are: %(missing_info)s")
        raise exception.MissingParameterValue(
            exc_msg % {'error_msg': error_msg, 'missing_info': missing_info})


def _parse_driver_info(driver):
    info = driver.driver_info
    d_info = {k: info.get(k) for k in COMMON_PROPERTIES}
    error_msg = _("Cannot validate Generic Driver. Some parameters were"
                  " missing in the configuration file.")
    _check_for_missing_params(d_info, error_msg)
    return d_info


class GENERICDRIVER(base.BaseDriver):

    def __init__(self, execute=putils.execute, *args, **kwargs):
        self.host = kwargs.get('host')
        self.backend = kwargs.get('backend')
        self.driver_type = kwargs.get('driver_type')
        self._execute = execute

    def get_properties(self):
        """Return the properties of the generic driver.

        :returns: dictionary of <property name>:<property description> entries.
        """
        return COMMON_PROPERTIES

    def install_driver(self, driver_type):

            def attach_instance(self, instance_id):
                pass

    def uninstall_driver(self, driver_type):

            def detach_instance(self, instance_id):
                pass

            def delete(self):
                pass

    def discover_driver(self, driver_type):
        pass

    def driver_list(self, driver_type):
        pass

    def update(self, driver_type):
        pass

    def do_setup(self):
        self._execute('sudo', './setup.sh')