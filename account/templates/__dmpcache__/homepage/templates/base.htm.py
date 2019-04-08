# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554750122.3340979
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'menu', 'site_left', 'site_center']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        def site_left():
            return render_site_left(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def menu():
            return render_menu(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/favicon.ico" type="image/x-icon" />\r\n        <title>Intex &mdash; ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n\r\n')
        __M_writer('        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/bootstrap.min.css">\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/bootstrap.min.js"></script>\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer(' \r\n    </head>\r\n    <body>\r\n        <header id="header">\r\n            <nav class="navbar navbar-expand-lg">\r\n                <a href="/"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/logo.png" alt="home" /></a>\r\n')
        __M_writer('                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n            </nav>\r\n        </header>\r\n\r\n        <main>\r\n            <div id="site_left">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </main>\r\n\r\n         ')
        __M_writer('\r\n        <footer>\r\n            &copy; Copyright ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(datetime.now().year))
        __M_writer('\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">\r\n                        <span class="icon-bar"></span>\r\n                        <span class="icon-bar"></span>\r\n                        <span class="icon-bar"></span> \r\n                    </button>\r\n                    <div class="dropdown collapse navbar-collapse" id="myNavbar">        \r\n                        <ul class="nav navbar-nav">\r\n                            <li><a class="dropdown-item nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'index' else ''))
        __M_writer('" href="/">Home</a></li>\r\n                        </ul>\r\n                        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                            Welcome')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(',' if user.username != '' else ''))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(user.username))
        __M_writer('\r\n                        </button>\r\n                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">\r\n')
        if user.is_authenticated: 
            __M_writer('                                <a class="dropdown-item nav-link" href="/account/logout">Logout</a>\r\n                                <a class="dropdown-item nav-link" href="/account/preferences">Account</a>\r\n')
        else: 
            __M_writer('                                <a class="dropdown-item nav-link" href="/account/login">Login</a>\r\n')
        __M_writer('                        </div>\r\n                    </div>        \r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    <div class="search">\r\n                        <input type="text" id="mySearch" placeholder="Search.." title="Type in a category">\r\n                        <button type="submit" class="searchButton">\r\n                            <p class="btn-search">GO</p>\r\n                        </button>\r\n                    </div>\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    \r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 68, "20": 0, "37": 2, "38": 7, "39": 7, "44": 8, "45": 11, "46": 11, "47": 11, "48": 12, "49": 12, "50": 13, "51": 13, "52": 16, "53": 17, "54": 17, "55": 22, "56": 22, "57": 24, "62": 46, "67": 59, "72": 64, "73": 68, "74": 70, "75": 70, "81": 8, "92": 24, "101": 24, "102": 32, "103": 32, "104": 35, "105": 35, "106": 35, "107": 35, "108": 38, "109": 39, "110": 41, "111": 42, "112": 44, "118": 52, "124": 52, "130": 62, "136": 62, "142": 136}}
__M_END_METADATA
"""
