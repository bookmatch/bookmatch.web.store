import unittest
from unittest import mock
import webtest
from testfixtures import compare, Comparison as C


class TestApp(unittest.TestCase):

    def test_index(self):
        from bookmatch.web.store import main
        app = main({})
        app = webtest.TestApp(app)

        res = app.get("/")
