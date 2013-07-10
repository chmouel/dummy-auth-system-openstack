# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Spanish National Research Council
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import os

from keystoneclient import auth_plugin
from keystoneclient import exceptions

def env(*vars, **kwargs):
    """Search for the first defined of possibly many env vars

    Returns the first environment variable defined in vars, or
    returns the default defined in kwargs.

    """
    for v in vars:
        value = os.environ.get(v, None)
        if value:
            return value
    return kwargs.get('default', '')


class DummyAuthPlugin(auth_plugin.BaseAuthPlugin):
    def __init__(self):
        self.opts = {}

    def parse_opts(self, args):
        dummy_arg = args.dummy_arg
        if not dummy_arg:
            raise exceptions.CommandError("You requested to use the 'dummy' "
                                          "auth system, which very usefully "
                                          "would print something before you "
                                          "connect. Please specify something "
                                          "to print in the dummy arg.")

        self.opts = {"dummy_arg": dummy_arg}
        return self.opts

    @staticmethod
    def add_opts(parser):
        parser.add_argument('--dummy-arg',
                            metavar='<dummy-arg>',
                            default=env('DUMMY_ARG', default=None),
                            help=("Dummy plugin which print stuff. "
                                  "Defaults to env[DUMMY_ARG]."))
        return parser

    def authenticate(self, cls, auth_url, **kwargs):
        """Print dummy stuff."""
        dummy_arg = self.opts.get("dummy_arg", None)
        if dummy_arg:
            print dummy_arg
        return cls._base_authN(auth_url, **kwargs)
