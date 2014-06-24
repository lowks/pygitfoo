"""
Repository info logic.
"""
from pygitfoo import raw_data_operations

from pygitfoo.system_commands import run_system_command

__author__ = 'lmiranda'


class RepositoryInfo(object):
    """
    Provides info about a repository.
    """

    def __init__(self, path, name):
        """
        Initiates a repository named 'name' in path 'path'.

        :param path: The path where the repository is located.
        :param name: The name of the repository.
        """

        self.path = path
        self.name = name
        self.repository_path = "%s/%s" % (self.path, self.name)
        
    def tag(self):
        """
        List all tags.
        """
        
        raw_tags = run_system_command("git tag", self.repository_path) 

        return raw_data_operations.process_tags(raw_tags)

    def branch(self):
        """
        Lists local branches.
        """

        raw_branches = run_system_command("git branch", self.repository_path)

        return raw_data_operations.process_branches(raw_branches)

    def current_branch(self):
        """
        Gets current branch.
        """

        raw_branches = run_system_command("git branch", self.repository_path)

        return raw_data_operations.process_current_branch(raw_branches)

    def ls_remote(self):
        """
        Gets a list of tags in the remote.
        """

        raw_tags = run_system_command("git ls-remote", self.repository_path)

        return raw_data_operations.process_ls_remote(raw_tags)