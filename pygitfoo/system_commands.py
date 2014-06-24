"""
Direct interaction with system.
"""

import subprocess

__author__ = 'lmiranda'


def run_system_command(command, cwd=None):
    """
    Runs a command in the specified directory.
    
    :param command: The command to be executed.
    :param cwd: The directory were the command should be executed.
    """

    p = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, cwd=cwd)
    out, err = p.communicate()
    if err:
        raise Exception(str(err))

    return out