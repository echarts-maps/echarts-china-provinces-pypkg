# flake8: noqa
import os

from echarts_china_provinces_pypkg._version import __version__
from echarts_china_provinces_pypkg._version import __author__
from lml.plugin import PluginInfo


@PluginInfo('pyecharts_js_extension', tags=['custom'])
class Pypkg():
    def __init__(self):
        __package_path__ = os.path.dirname(__file__)
        self.js_extension_path = os.path.join(
            __package_path__, "resources")
