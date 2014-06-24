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

    def branch(self):
        """
        Lists local branches.
        """

        raw_branches = run_system_command("git branch", self.repository_path)
        branches = raw_branches.split('\n')[0:-1]
        branches = [branch.strip('  ').strip('* ') for branch in branches]

        return branches

    def current_branch(self):
        """
        Gets current branch.
        """

        return run_system_command("git branch", self.repository_path)[0].split(' ')[-1]

    def list_remote_tags(self):
        """
        Gets list of tags in the remote.
        """

        ret = run_system_command("git ls-remote --tags", self.repository_path)
        tag_list = []
        for line in ret:
            print line
            if "tags" in line:
                tag_list.append(line.split("/")[-1])

        return tag_list

    def most_recent_lightweight_tag(self):
        """
        Gets the current the most tag in the repository.
        """

        return run_system_command("git describe --tags", self.repository_path)[0]
