# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555469756.3912396
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/bp/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['menu', 'content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>DMP</title>\r\n\r\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/bootstrap.min.css">\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/bootstrap.min.js"></script>\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n        <header id="header">\r\n            <nav class="navbar navbar-expand-lg">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n            </nav>\r\n        </header>\r\n\r\n        <main>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </main>\r\n\r\n        <footer>\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        self = context.get('self', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">\r\n                        <span class="icon-bar"></span>\r\n                        <span class="icon-bar"></span>\r\n                        <span class="icon-bar"></span> \r\n                    </button>\r\n                    <div class="dropdown collapse navbar-collapse" id="myNavbar">        \r\n                        <ul class="nav navbar-nav">\r\n                            <li><a class="dropdown-item nav-link" href="/bp/index/">Home</a></li>\r\n                        </ul>\r\n                        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                            Welcome')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(',' if user.username != '' else ''))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(user.username))
        __M_writer('\r\n                        </button>\r\n                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">\r\n')
        if user.is_authenticated: 
            __M_writer('                                <a class="dropdown-item nav-link" href="/bp/logout">Logout</a>\r\n')
        else: 
            __M_writer('                                <a class="dropdown-item nav-link" href="/bp/login">Login</a>\r\n')
        __M_writer('                        </div>\r\n                    </div> \r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                Site content goes here in sub-templates.\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/bp/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "30": 2, "31": 10, "32": 12, "33": 12, "34": 13, "35": 13, "36": 14, "37": 14, "38": 17, "39": 18, "40": 18, "45": 45, "50": 52, "56": 24, "64": 24, "65": 35, "66": 35, "67": 35, "68": 35, "69": 38, "70": 39, "71": 40, "72": 41, "73": 43, "79": 50, "85": 50, "91": 85}}
__M_END_METADATA
"""
