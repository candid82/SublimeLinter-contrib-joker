#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Roman Bataev
# Copyright (c) 2017 Roman Bataev
#
# License: MIT
#

"""This module exports the Joker plugin class."""

from SublimeLinter.lint import Linter, util


class Joker(Linter):
    """Provides an interface to joker."""

    executable = 'joker'

    def cmd(self):
        """Return the command to run."""
        if self.filename.endswith('.joke'):
            return 'joker --lintjoker --working-dir ${file} -'
        elif self.filename.endswith('.cljs'):
            return 'joker --lintcljs --working-dir ${file} -'
        elif self.filename.endswith('.edn') or self.filename.endswith('.joker'):
            return 'joker --lintedn --working-dir ${file} -'
        else:
            return 'joker --lintclj --working-dir ${file} -'

    # stdin:88:13: Read error: Invalid unicode escape: \uqwer
    regex = r'<stdin>:(?P<line>\d+):(?P<col>\d+): (?P<message>.*((?P<error>error|Exception)|(?P<warning>warning)).*)'

    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    word_re = r'^([-\w\.]+)'
    defaults = {
        'selector': 'source.clj, source.cljs, source.edn'
    }
    inline_settings = None
    inline_overrides = None
    comment_re = None
    on_stderr = None
