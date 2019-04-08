# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554752856.393814
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'menu', 'site_center', 'site_right']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
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
        

        __M_writer('\r\n            </nav>\r\n        </header>\r\n\r\n        <main>\r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_right">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </main>\r\n    </body>\r\n</html>\r\n')
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
        user = context.get('user', UNDEFINED)
        def menu():
            return render_menu(context)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
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


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    <div class="search">\r\n                        <input type="text" id="mySearch" placeholder="Search.." title="Type in a category">\r\n                        <button type="submit" class="searchButton">\r\n                            <p class="btn-search">GO</p>\r\n                        </button>\r\n                    </div>\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "35": 2, "36": 7, "37": 7, "42": 8, "43": 11, "44": 11, "45": 11, "46": 12, "47": 12, "48": 13, "49": 13, "50": 16, "51": 17, "52": 17, "53": 22, "54": 22, "55": 24, "60": 46, "65": 54, "70": 64, "76": 8, "87": 24, "96": 24, "97": 32, "98": 32, "99": 35, "100": 35, "101": 35, "102": 35, "103": 38, "104": 39, "105": 41, "106": 42, "107": 44, "113": 52, "119": 52, "125": 57, "131": 57, "137": 131}}
__M_END_METADATA
"""
