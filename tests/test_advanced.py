# -*- coding: utf-8 -*-

from .context import blockchain

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_example(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
