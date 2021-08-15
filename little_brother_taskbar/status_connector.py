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

from little_brother_taskbar import constants
from little_brother_taskbar import user_status
from python_base_app import base_rest_api_access
from python_base_app import exceptions
from python_base_app import tools

SECTION_NAME = "StatusConnector"


class StatusConnectorConfigModel(base_rest_api_access.BaseRestAPIAccessConfigModel):

    def __init__(self):
        """Class to configure the class `StatusConnector`."""
        super().__init__(p_section_name=SECTION_NAME)


class StatusConnector(base_rest_api_access.BaseRestAPIAccess):

    def __init__(self, p_config, p_lang):
        """Class to request the user status from a LittleBrother master process."""
        super().__init__(
            p_config=p_config,
            p_base_api_url=constants.API_URL,
            p_section_name=SECTION_NAME)

        self._ = p_lang

    def request_status(self, p_username):

        url = self._get_api_url(constants.API_REL_URL_STATUS)

        try:
            api_result = self.execute_api_call(
                p_url=url,
                p_method="GET",
                # p_mime_type="application/json",
                p_parameters={constants.API_URL_PARAM_USERNAME: p_username},
                p_jsonify=True)

            result = tools.objectify_dict(p_dict=api_result,
                                          p_class=user_status.UserStatus,
                                          p_attribute_classes={})

        except exceptions.ArtifactNotFoundException as e:
            if e.result_document is not None:
                fmt = self._(e.result_document[constants.JSON_ERROR])

            else:
                fmt = self._("Cannot request user status using url '{url}'")

            result = fmt.format(username=p_username, url=self._get_api_url())
            self._logger.warning(result)

        except Exception:

            fmt = self._("Cannot request user status using url '{url}'")
            result = fmt.format(url=self._get_api_url())
            self._logger.error(result)

        return result

    def request_time_extension(self, p_username:str, p_extension_length:int, p_secret:str):

        url = self._get_api_url(constants.API_REL_URL_REQUEST_TIME_EXTENSION)

        api_result = None

        try:
            api_result = self.execute_api_call(
                p_url=url,
                p_method="POST",
                # p_mime_type="application/json",
                p_parameters={
                    constants.API_URL_PARAM_USERNAME: p_username,
                    constants.API_URL_PARAM_EXTENSION_LENGTH: str(p_extension_length),
                    constants.API_URL_PARAM_SECRET: p_secret
                })

        except exceptions.ArtifactNotFoundException as e:
            if e.result_document is not None:
                fmt = self._(e.result_document[constants.JSON_ERROR])

            else:
                fmt = self._("Cannot request time extension using url '{url}'")

            result = fmt.format(username=p_username, url=self._get_api_url())
            self._logger.warning(result)

        except Exception as e:

            fmt = self._("Error while requesting time extension: '{msg}'")
            result = fmt.format(msg=str(e))
            self._logger.error(result)

        return api_result

