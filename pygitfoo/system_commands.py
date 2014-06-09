"""
Direct interaction with system.
"""

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

    return out.split('\n')