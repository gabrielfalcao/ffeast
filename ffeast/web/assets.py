# -*- coding: utf-8 -*-
# flake8: noqa
from __future__ import absolute_import

from flask.ext.assets import (
    Bundle,
)

from ffeast.base.assets import jquery, angular, uikit_js, uikit_css

web_scripts = Bundle('js/*.js')
web_css = Bundle('less/*.less', filters=('recess',))

BUNDLES = [
    ('js-web', Bundle(jquery, angular, web_scripts, filters=('uglifyjs',), output='ffeast.js')),
    ('css-web', Bundle(uikit_css, web_css, output='ffeast.css')),
]
