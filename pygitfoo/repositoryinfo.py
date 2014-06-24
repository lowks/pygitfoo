"""
Repository info logic.
"""

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
        
        return raw_tags.split('\n')[0:-1]

    def _get_raw_branches_to_list(self):
        raw_branches = run_system_command("git branch", self.repository_path)
        branches = raw_branches.split('\n')[0:-1]

        return branches

    def branch(self):
        """
        Lists local branches.
        """

        branches = self._get_raw_branches_to_list()
        branches = [branch.strip('  ').strip('* ') for branch in branches]

        return branches

    def current_branch(self):
        """
        Gets current branch.
        """

        branches = self._get_raw_branches_to_list()
        branch = [branch.strip('* ') for branch in branches if branch.startswith('* ')]

        return branch

    def ls_remote(self):
        """
        Gets a list of tags in the remote.
        """

        ret = run_system_command("git ls-remote", self.repository_path)
        tag_list = [tag.split('/')[-1] for tag in ret.split('\n') if "/tags/" in tag]

        return tag_list