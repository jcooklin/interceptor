# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from interceptor.openstack.common import log as logging


logger = logging.getLogger(__name__)


class classproperty(property):
    """
    Class decorator to implement a property for the class (not class instance)

    Usage:
    @classproperty
    def some_property(cls):
        return some_value
    """
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()
