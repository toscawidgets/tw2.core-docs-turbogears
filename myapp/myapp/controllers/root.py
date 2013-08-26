# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from myapp.model import DBSession, metadata

from myapp.lib.base import BaseController
from myapp.controllers.error import ErrorController
from myapp.controllers.movie import MovieController

__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the myapp application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """

    error = ErrorController()
    movie = MovieController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "myapp"

    @expose('myapp.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('myapp.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('myapp.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(page='environ', environment=request.environ)

    @expose('myapp.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(page='data', params=kw)
