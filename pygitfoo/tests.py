import unittest
from raw_data_operations import  *

__author__ = 'lmiranda'


class TestRawDataOperations(unittest.TestCase):

    def test_tag(self):

        raw_data = "0.1.1dev\n0.1dev\n0.2.0dev\n"
        tags = process_tags(raw_data)

        self.assertEqual(['0.1.1dev', '0.1dev', '0.2.0dev'], tags, "Tags do not match: %s" % tags)

    def test_branch(self):

        raw_data = "  develop\n* feature/0.3.0dev\n  feature/0.4.0dev\n  master\n"
        branches = process_branches(raw_data)

        self.assertEqual(['develop', 'feature/0.3.0dev', 'feature/0.4.0dev', 'master'],
                         branches, "Branches do not match: %s" % branches)

    def test_current_branch(self):

        raw_data = "  develop\n* feature/0.3.0dev\n  feature/0.4.0dev\n  master\n"
        branches = process_current_branch(raw_data)

        self.assertEqual(['feature/0.3.0dev'], branches, "Current branch does not match: %s" % branches)

    def test_ls_remote(self):

        raw_data = "15ff9ac584a0c00dabd88aa8066ad8ca6d0cb9af	refs/tags/0.1.1dev\n" +\
                   "cc32de100599a6a85dcb4171a10b88ead5d5f0fc	refs/tags/0.1dev\n" +\
                   "c2b84d67f8e60aaa31194d0da15ba953c605c9de	refs/tags/0.2.0dev\n"

        branches = process_ls_remote(raw_data)

        self.assertEqual(['0.1.1dev', '0.1dev', '0.2.0dev'], branches, "Remote branches do not match: %s" % branches)