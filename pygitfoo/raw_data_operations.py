"""
Processes git commands output.
"""

__author__ = 'lmiranda'


def process_tags(raw_data):

    return raw_data.split('\n')[0:-1]


def process_branches(raw_data):

    branches = raw_data.split('\n')[0:-1]

    return [branch.strip('  ').strip('* ') for branch in branches]


def process_current_branch(raw_data):

    branches = raw_data.split('\n')[0:-1]
    return [branch.strip('* ') for branch in branches if branch.startswith('* ')]


def process_ls_remote(raw_data):

    return [tag.split('/')[-1] for tag in raw_data.split('\n') if "/tags/" in tag]