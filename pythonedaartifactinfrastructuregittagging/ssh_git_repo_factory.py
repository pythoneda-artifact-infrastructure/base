"""
pythonedaartifactinfrastructuregittagging/ssh_git_repo_factory.py

This file declares the SshGitRepoFactory class.

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
from pythonedaartifactgittagging.git_repo_factory import GitRepoFactory
from pythonedasharedgit.git_repo import GitRepo


class SshGitRepoFactory(GitRepoFactory):
    """
    An implementation of GitRepoFactory that gets the SSH details from the command line.

    Class name: SshGitRepoFactory

    Responsibilities:
        - Builds GitRepo instances using extra SSH information from the command line.

    Collaborators:
        - None
    """

    @classmethod
    def ssh_username(cls, username: str):
        """
        Specifies the SSH username.
        :param username: Such value.
        :type username: str
        """
        cls._ssh_username = username

    @classmethod
    def privateKey(cls, privateKey: str):
        """
        Specifies the location of the private key.
        :param privateKey: Such value.
        :type privateKey: str
        """
        cls._privateKey = privateKey

    @classmethod
    def passphrase(cls, passphrase: str):
        """
        Specifies the private key passphrase.
        :param passphrase: Such value.
        :type passphrase: str
        """
        cls._passphrase = passphrase

    def create(self, repositoryUrl: str, head: str) -> GitRepo:
        """
        Creates a GitRepo instance.
        :param repositoryUrl: The url of the repository.
        :type repositoryUrl: str
        :param head: The head to point to.
        :type head: str
        :return: The GitRepo.
        :rtype: GitRepo from pythonedasharedgit.git_repo
        """
        return
