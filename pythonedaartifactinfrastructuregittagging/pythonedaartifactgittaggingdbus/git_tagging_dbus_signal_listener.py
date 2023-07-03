"""
pythonedaartifactinfrastructuregittagging/pythonedaartifactgittaggingdbus/git_tagging_dbus_signal_listener.py

This file defines the GitTaggingDbusSignalListener class.

Copyright (C) 2023-today rydnr's pythoneda-artifact-infrastructure/git-tagging

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.event import Event
from pythonedaartifacteventgittagging.tag_credentials_provided import TagCredentialsProvided
from pythonedainfrastructure.pythonedadbus.dbus_signal_listener import DbusSignalListener
from pythonedaartifacteventinfrastructuregittagging.pythonedaartifacteventgittaggingdbus.dbus_tag_credentials_provided import DbusTagCredentialsProvided

from dbus_next import BusType, Message

from typing import Dict

class GitTaggingDbusSignalListener(DbusSignalListener):

    """
    A Port that listens to GitTagging-relevant d-bus signals.

    Class name: GitTaggingDbusSignalListener

    Responsibilities:
        - Connect to d-bus.
        - Listen to signals relevant to GitTagging.

    Collaborators:
        - PythonEDAApplication: Receives relevant domain events.
    """

    def __init__(self):
        """
        Creates a new GitTaggingDbusSignalListener instance.
        """
        super().__init__()

    def signal_receivers(self, app) -> Dict:
        """
        Retrieves the configured signal receivers.
        :param app: The PythonEDA instance.
        :type app: PythonEDA from pythonedaapplication.pythoneda
        :return: A dictionary with the signal name as key, and the tuple interface and bus type as the value.
        :rtype: Dict
        """
        result = {}
        key = self.fqdn_key(TagCredentialsProvided)
        result[key] = [
            DbusTagCredentialsProvided, BusType.SYSTEM, self.listen_TagCredentialsProvided.__name__
        ]
        return result

    def parse_TagCredentialsProvided(self, message: Message) -> TagCredentialsProvided:
        """
        Parses given d-bus message containing a TagCredentialsProvided event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The TagCredentialsProvided event.
        :rtype: pythonedaartifactgittagging.tag_credentials_provided.TagCredentialsProvided
        """
        request_id, repository_url, branch, ssh_username, private_key_file, private_key_passphrase = message.body
        return TagCredentialsProvided(request_id, repository_url, branch, ssh_username, private_key_file, private_key_passphrase)

    async def listen_TagCredentialsProvided(self, event: TagCredentialsProvided):
        """
        Gets notified when a TagCredentialsProvided event occurs.
        :param event: The TagCredentialsProvided event.
        :type event: pythonedaartifactgittagging.tag_credentials_provided.TagCredentialsProvided
        """
        print(f'Received TagCredentialsProvided {event}')
        await self.app.accept(event)
