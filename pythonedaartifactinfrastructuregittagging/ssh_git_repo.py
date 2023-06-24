"""
pythonedaartifactinfrastructuregittagging/ssh_git_repo.py

This file declares the SshGitRepo class.

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
from pythonedasharedgit.git_repo import GitRepo

class SshGitRepo(GitRepo):
    """
    Represents a Git repository accessed via SSH.

    Class name: SshGitRepo

    Responsibilities:
        - Represents a SSH-accesible git repository and its metadata.

    Collaborators:
        - GitRepo: To provide the core functionality.
    """

    def __init__(self, url: str, rev: str, sshUsername: str, privateKey: str, passphrase: str):
        """
        Creates a new Git repository instance.
        :param url: The url of the repository.
        :type url: str
        :param rev: The revision.
        :type rev: str
        :param sshUsername: The SSH username.
        :type sshUsername: str
        :param privateKey: The private key for SSH authentication.
        :type privateKey: str
        :param passphrase: The passphrase of the private key.
        :type passphrase: str
        """
        super().__init__(url, rev)
        self._username = sshUsername
        self._private_key = privateKey
        self._passphrase = passphrase

    @property
    @attribute
    def username(self) -> str:
        """
        Retrieves the SSH username.
        :return: Such value.
        :rtype: str
        """
        return self._username

    @property
    @attribute
    @sensitive
    def private_key(self) -> str:
        """
        Retrieves the path of the private key file.
        :return: Such path.
        :rtype: str
        """
        return self._private_key

    @property
    @attribute
    @sensitive
    def passphrase(self) -> str:
        """
        Retrieves the passphrase.
        :return: Such value.
        :rtype: str
        """
        return self._passphrase

    def clone(self) -> Repo:
        """
        Clones this repo.
        :return: A git.Repo instance.
        :rtype: git.Repo
        """
        return clone(self.url, self.rev, self.username, self.private_key, self.passphrase)
