#!/usr/bin/env python

"""Tests for `pdf_remove_duplicate_pages` package."""


import unittest
from click.testing import CliRunner

from pdf_remove_duplicate_pages import pdf_remove_duplicate_pages
from pdf_remove_duplicate_pages import cli


class TestPdf_remove_duplicate_pages(unittest.TestCase):
    """Tests for `pdf_remove_duplicate_pages` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'pdf_remove_duplicate_pages.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
