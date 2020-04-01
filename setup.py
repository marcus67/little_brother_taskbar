# -*- coding: utf-8 -*-

#    Copyright (C) 2019  Marcus Rickert
#
#    See https://github.com/marcus67/little_brother_taskbar
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os

from setuptools import setup

import little_brother_taskbar.settings

# See https://stackoverflow.com/questions/26900328/install-dependencies-from-setup-py

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []

if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setup_params = {
    # standard setup configuration

    "install_requires": [
        'python-base-app',
        'jinja2',
        'wxPython'],

    "packages": ['little_brother_taskbar', 'little_brother_taskbar.test'],

    "include_package_data": True,

    "scripts": [
        "run_little_brother_taskbar",
    ],
    "long_description": "Taskbar application for window manager tray to display status "
                        "of users monitored by LittleBrother",
}

extended_setup_params = {
    # additional setup configuration used by CI stages

    # technical name used for e.g. directories, PIP-package, and users
    "build_debian_package" : False,

    "contributing_setups": ["python_base_app"],
}

setup_params.update(little_brother_taskbar.settings.settings)
extended_setup_params.update(little_brother_taskbar.settings.extended_settings)
extended_setup_params.update(setup_params)

if __name__ == '__main__':
    setup(**setup_params)
