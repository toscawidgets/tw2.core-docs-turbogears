# -*- coding: utf-8 -*-
"""
Functional test suite for the root controller.

This is an example of how functional tests can be written for controllers.

As opposed to a unit-test, which test a small unit of functionality,
functional tests exercise the whole application and its WSGI stack.

Please read http://pythonpaste.org/webtest/ for more information.

"""

from nose.tools import ok_

from myapp.tests import TestController


class TestRootController(TestController):
    """Tests for the method in the root controller."""

    def test_index(self):
        """The front page is working properly"""
        response = self.app.get('/')
        msg = 'TurboGears 2 is rapid web application development toolkit '\
              'designed to make your life easier.'
        # You can look for specific strings:
        ok_(msg in response)

        # You can also access a BeautifulSoup'ed response in your tests
        # (First run $ easy_install BeautifulSoup
        # and then uncomment the next two lines)

        # links = response.html.findAll('a')
        # print links
        # ok_(links, "Mummy, there are no links here!")

    def test_environ(self):
        """Displaying the wsgi environ works"""
        response = self.app.get('/environ.html')
        ok_('The keys in the environment are: ' in response)

    def test_data(self):
        """The data display demo works with HTML"""
        response = self.app.get('/data.html?a=1&b=2')
        expected1 = """<td>a</td>\n                <td>1</td>"""
        expected2 = """<td>b</td>\n                <td>2</td>"""
        body = '\n'.join(response.text.splitlines())
        ok_(expected1 in body, response)
        ok_(expected2 in body, response)

    def test_data_json(self):
        """The data display demo works with JSON"""
        resp = self.app.get('/data.json?a=1&b=2')
        ok_(dict(page='data', params={'a':'1', 'b':'2'}) == resp.json, resp.json)

