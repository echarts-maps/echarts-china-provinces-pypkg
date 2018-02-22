# -*- coding: utf-8 -*-
DESCRIPTION = (
    'Python package for chinese provinces for pyecharts' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'echarts-china-provinces-pypkg'
copyright = u'2018 pyecharts dev team'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'echarts-china-provinces-pypkgdoc'
latex_elements = {}
latex_documents = [
    ('index', 'echarts-china-provinces-pypkg.tex',
     'echarts-china-provinces-pypkg Documentation',
     'pyecharts dev team', 'manual'),
]
man_pages = [
    ('index', 'echarts-china-provinces-pypkg',
     'echarts-china-provinces-pypkg Documentation',
     [u'pyecharts dev team'], 1)
]
texinfo_documents = [
    ('index', 'echarts-china-provinces-pypkg',
     'echarts-china-provinces-pypkg Documentation',
     'pyecharts dev team', 'echarts-china-provinces-pypkg',
     DESCRIPTION,
     'Miscellaneous'),
]
