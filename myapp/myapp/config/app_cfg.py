# -*- coding: utf-8 -*-
"""
Global configuration file for TG2-specific settings in myapp.

This file complements development/deployment.ini.

Please note that **all the argument values are strings**. If you want to
convert them into boolean, for example, you should use the
:func:`paste.deploy.converters.asbool` function, as in::
    
    from paste.deploy.converters import asbool
    setting = asbool(global_conf.get('the_setting'))
 
"""

from tg.configuration import AppConfig

from tw2.core.middleware import ControllersApp as TW2ControllersApp

import myapp
from myapp import model
from myapp.lib import app_globals, helpers 

base_config = AppConfig()
base_config.renderers = []
base_config.prefer_toscawidgets2 = True

base_config.package = myapp

#Enable json in expose
base_config.renderers.append('json')
#Set the default renderer
base_config.default_renderer = 'mako'
base_config.renderers.append('mako')
#Configure the base SQLALchemy Setup
base_config.use_sqlalchemy = True
base_config.model = myapp.model
base_config.DBSession = myapp.model.DBSession

base_config.custom_tw2_config['controllers'] = TW2ControllersApp()
base_config.custom_tw2_config['controller_prefix'] = '/tw2_controllers/'
base_config.custom_tw2_config['serve_controllers'] = True
