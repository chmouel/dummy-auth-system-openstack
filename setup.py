# coding=utf-8

# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 eNovance
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
import setuptools


def read_file(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setuptools.setup(
    name="dummy-auth-system-openstack",
    version="1.0",
    author="Chmouel Boudjnah",
    author_email="chmouel@enovance.com",
    description="Dummy based authentication for Openstack",
    long_description=read_file("README.rst"),
    license="Apache License, Version 2.0",
    url="https://github.com/chmouel/dummy-auth-system-openstack",
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ],
    entry_points={
        "openstack.client.auth_plugin": [
            "dummy = dummy_auth_system_openstack.plugin:DummyAuthPlugin"
        ],
    }
)
