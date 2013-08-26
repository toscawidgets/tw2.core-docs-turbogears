# -*- coding: utf-8 -*-
"""Setup the myapp application"""
from __future__ import print_function

import logging
from tg import config
from myapp import model
import transaction

def bootstrap(command, conf, vars):
    """Place any commands to setup myapp here"""

    # <websetup.bootstrap.before.auth
    for name in ['Action', 'Comedy', 'Romance', 'Sci-fi']:
        model.DBSession.add(model.Genre(name=name))
    transaction.commit()
    # <websetup.bootstrap.after.auth>
