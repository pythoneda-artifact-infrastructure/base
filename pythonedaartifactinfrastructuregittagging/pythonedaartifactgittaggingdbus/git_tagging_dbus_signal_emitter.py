"""
pythonedaartifactinfrastructuregittagging/pythonedagittaggingdbus/git_tagging_dbus_signal_emitter.py

This file defines the GitTaggingDbusSignalEmitter class.

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
from pythonedaartifacteventgittagging.tag_credentials_requested import TagCredentialsRequested
from pythonedaartifacteventinfrastructuregittagging.pythonedaartifacteventgittaggingdbus.dbus_tag_credentials_requested import DbusTagCredentialsRequested
from pythonedainfrastructure.pythonedadbus.dbus_signal_emitter import DbusSignalEmitter

import asyncio
from dbus_next.aio import MessageBus
from dbus_next import BusType, Message, MessageType

from typing import Dict, List

class GitTaggingDbusSignalEmitter(DbusSignalEmitter):

    """
    A Port that emits GitTagging events as d-bus signals.

    Class name: GitTaggingDbusSignalEmitter

    Responsibilities:
        - Connect to d-bus.
        - Emit domain events as d-bus signals on behalf of GitTagging.

    Collaborators:
        - PythonEDAApplication: Requests emitting events.
    """
    def __init__(self):
        """
        Creates a new GitTaggingDbusSignalEmitter instance.
        """
        super().__init__()

    def transform_TagCredentialsRequested(self, event: TagCredentialsRequested) -> List:
        """
        Transforms given event to string.
        :param event: The event to transform.
        :type event: TagCredentialsProvided from pythonedaartifactgittagging.tag_credentials_requested
        :return: The serialized version of the event.
        :rtype: str
        """
        print(f'transformTagCredentialsRequested -> {[ event.repository_url, event.branch ]}')
        return [ event.repository_url, event.branch ]

    def signature_for_TagCredentialsRequested(self, event: TagCredentialsRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: interface=pythonedaartifacteventgittagging.tag_credentials_requested.TagCredentialsRequested;
        :return: The signature.
        :rtype: str
        """
        return 'ss'

    def emitters(self) -> Dict:
        """
        Retrieves the configured event emitters.
        :return: A dictionary with the event class name as key, and a dictionary as value. Such dictionary must include the following entries:
          - "interface": the event interface,
          - "busType": the bus type,
          - "destination": the event destination,
          - "path": the path,
          - "interfaceName": the interface name,
          - "signal": the signal name,
          - "transformer": a function capable of transforming the event into a string.
          - "signature": a function capable of returning the types of the event parameters.
        :rtype: Dict
        """
        result = {}
        key = self.fqdn_key(TagCredentialsRequested)
        result[key] = {
                "interface": DbusTagCredentialsRequested,
                "busType": BusType.SYSTEM,
                "destination": "pythoneda.artifact.git-tagging",
                "path": "/pythoneda/artifact/git_tagging",
                "interfaceName": "pythoneda.artifact.GitTagging",
                "signal": "TagCredentialsRequested",
                "transformer": self.transform_TagCredentialsRequested,
                "signature": self.signature_for_TagCredentialsRequested
            }

        return result
