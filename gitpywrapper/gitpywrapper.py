import subprocess

__author__ = 'lmiranda'


def _run_system_command(command, cwd=None):
    """
    Runs a command in the specified directory.
    """

    p = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, cwd=cwd)
    out, err = p.communicate()
    if err:
        raise Exception(str(err))

    return out.split('\n')[0]


class Git(object):
    """
    Git command.
    """

    @staticmethod
    def version():
        """
        Returns the version of the installed git.
        """

        ret = _run_system_command("git --version")
        return ret.split(' ')[-1]


class Repository(object):
    """
    Git repository.
    """

    def __init__(self, path, name):
        """
        Initiates a repository named 'name' in path 'path'.

        :param path: The path where the repository is located.
        :param name: The name of the repository.
        """

        self.path = path
        self.name = name

    def branch(self):
        """
        Shows current branch.
        """

        return _run_system_command("git branch", self.path + "/" + self.name).split(' ')[-1]