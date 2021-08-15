# -*- coding: utf-8 -*-

# Copyright (C) 2019  Marcus Rickert
#
# See https://github.com/marcus67/little_brother_taskbar
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os.path

API_URL = "/api"
API_REL_URL_EVENTS = "events"
API_URL_EVENTS = os.path.join(API_URL, API_REL_URL_EVENTS)

API_REL_URL_STATUS = "status"
API_URL_STATUS = os.path.join(API_URL, API_REL_URL_STATUS)

API_REL_URL_REQUEST_TIME_EXTENSION = "request-time-extension"
API_URL_REQUEST_TIME_EXTENSION = os.path.join(API_URL, API_REL_URL_REQUEST_TIME_EXTENSION)

API_URL_PARAM_USERNAME = "username"
API_URL_PARAM_SECRET = "secret"
API_URL_PARAM_EXTENSION_LENGTH = "extension_length"

JSON_HOSTNAME = "hostname"
JSON_EVENTS = "events"
JSON_RULESETS = "rulesets"
JSON_USERNAME = "username"
JSON_PROCESS_NAME_PATTERN = "process_name_pattern"
JSON_ACCESS_TOKEN = "sec" + "ret"
JSON_ERROR = "error"

HTTP_STATUS_CODE_OK = 200
HTTP_STATUS_CODE_UNAUTHORIZED = 401
HTTP_STATUS_CODE_NOT_FOUND = 404

TEMPLATE_STATUS_FIELD = "status_field.j2.html"

DEFAULT_ACCESS_CODE = "REPLACE-THIS-VALUE-WITH-A-STRONG-SECRET"

DEFAULT_WINDOW_HEIGHT_FACTOR_FOR_TIME_EXTENSION = 1.1
DEFAULT_WINDOW_HEIGHT_INCREASE_FOR_TIME_EXTENSION = 25
