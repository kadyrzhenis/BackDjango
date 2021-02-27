# Copyright (c) 2017 Andrew Bentley
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""Prompt for one of the databases contained in ~/.pgpass to connect to before launching psql"""

import os
import re
import shlex

import subprocess
from collections import OrderedDict

from fuzzyfinder.main import fuzzyfinder
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.shortcuts import create_prompt_application, run_application

__author__ = 'Andrew Bentley <andrew@bentley.codes>'
__version__ = '0.0.4'


DEFAULT_PGPASS_PATH = os.path.join(os.path.expanduser('~'), '.pgpass')
DEFAULT_PORT = '5432'
PGPASS_ENV = 'PGPASSFILE'
ENTRY_RE = re.compile(r'^(.*[^\\])?:(.*[^\\])?:(.*[^\\])?:(.*[^\\])?:(.*[^\\])?$')
PSQL_COMMAND = r'psql -h {hostname} -p {port} -U {username} {database}'
PROMPT = 'Connect to: '


class PgPassEntry:
    def __init__(self, hostname, port, database, username, password):
        self.hostname = hostname
        self.port = port
        self.database = database
        self.username = username
        self.password = password

    def get_dsn(self):
        if self.port == DEFAULT_PORT:
            return f'{self.username}@{self.hostname}/{self.database}'
        else:
            return f'{self.username}@{self.hostname}:{self.port}/{self.database}'


class PgPass:
    def __init__(self):
        self.entries = OrderedDict()

    def get_dsns(self):
        return self.entries.keys()

    def get_entry_from_dsn(self, dsn):
        return self.entries.get(dsn)

    @staticmethod
    def from_file(pgpass_path=None):
        if pgpass_path is None:
            if os.environ.get(PGPASS_ENV):
                pgpass_path = os.environ[PGPASS_ENV]
            else:
                pgpass_path = DEFAULT_PGPASS_PATH

        pg_pass = PgPass()
        with open(pgpass_path, 'r') as pgpass_file:
            for entry in pgpass_file:
                match = ENTRY_RE.match(entry)
                if match:
                    entry = PgPassEntry(*match.groups())
                    pg_pass.entries[entry.get_dsn()] = entry
        return pg_pass


class FuzzyCompleter(Completer):
    def __init__(self, words):
        self.words = words

    def get_completions(self, document, complete_event):
        suggestions = fuzzyfinder(document.text, self.words)
        for suggestion in suggestions:
            yield Completion(suggestion, start_position=-len(document.text))


def main():
    pgpass = PgPass.from_file()
    application = create_prompt_application(
        message=PROMPT,
        completer=FuzzyCompleter(pgpass.get_dsns()))
    application.on_start = lambda cli: cli.start_completion()
    dsn = run_application(application)

    entry = pgpass.get_entry_from_dsn(dsn)
    if entry:
        cmd = PSQL_COMMAND.format(
            hostname=entry.hostname,
            port=entry.port,
            username=entry.username,
            database=entry.database
        )
        subprocess.run(shlex.split(cmd))
    else:
        exit(1)


if __name__ == '__main__':
    main()
