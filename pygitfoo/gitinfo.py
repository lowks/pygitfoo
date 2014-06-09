"""
Git command related logic.
"""

from pygitfoo.system_commands import _run_system_command

__author__ = 'lmiranda'


class GitInfo(object):
    """
    Provides info about git software.
    """

    @staticmethod
    def installed_version():
        """
        Returns the version of the installed git.
        """

        ret = _run_system_command("git --version")
        return ret[0].split(' ')[-1]