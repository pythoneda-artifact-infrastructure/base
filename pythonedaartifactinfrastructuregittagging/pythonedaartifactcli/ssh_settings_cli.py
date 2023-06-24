"""
pythonedaartifactinfrastructuregittagging/pythonedaartifactcli/ssh_settings_cli.py

This file defines the SshSettingsCli class.

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
from pythoneda.primary_port import PrimaryPort

import argparse
import logging


class SshSettingsCli(PrimaryPort):

    """
    A PrimaryPort that provides the SSH settings for git operations.
    """

    def priority(self) -> int:
        return 100

    async def accept(self, app):
        """
        Processes the command specified from the command line.
        :param app: The PythonEDA instance.
        :type app: PythonEDA
        """
        parser = argparse.ArgumentParser(description="SSH settings")
        parser.add_argument("-U", "--ssh-user", required=True, help="The SSH username")
        parser.add_argument("-p", "--private-key", required=True, help="The path to the SSH private key")
        parser.add_argument("-P", "--private-key-passphrase", required=True, help="The passphrase of the SSH private key")
        args, unknown_args = parser.parse_known_args()

        await app.accept_ssh_settings(args.ssh_user, args.private_key, args.private_key_passphrase)
