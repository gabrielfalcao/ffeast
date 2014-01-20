#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright © 2013 Gabriel Falcão <gabriel@weedlabs.io>
#
from __future__ import unicode_literals, absolute_import

"""
ffeast.commands.db
~~~~~~~~~~~~~~~~~~~~~~

Contains commands for handling db stuff in the local environment
"""

import os
from flask.ext.script import Command



class CreateDB(Command):  # pragma: no cover
    def __init__(self, application):
        self.application = application

    def run(self):
        print "Creating database `ffeast`"
        os.system('echo "DROP DATABASE IF EXISTS ffeast" | mysql -uroot ')
        os.system('echo "CREATE DATABASE ffeast" | mysql -uroot ')
        print "Running migrations"
        os.system('alembic upgrade head')
