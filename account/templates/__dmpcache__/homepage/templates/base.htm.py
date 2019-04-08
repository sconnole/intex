# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554740851.7503076
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'dangerText', 'infoText', 'successText', 'warningText', 'menu', 'site_left', 'site_center', 'site_right']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def successText():
            return render_successText(context._locals(__M_locals))
        def infoText():
            return render_infoText(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        def site_left():
            return render_site_left(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def warningText():
            return render_warningText(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def dangerText():
            return render_dangerText(context._locals(__M_locals))
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
        __M_writer(' \r\n    </head>\r\n    <body>\r\n        <div class="alertContainer header_maintainence" id="alert">\r\n            <div class="alert danger">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'dangerText'):
            context['self'].dangerText(**pageargs)
        

        __M_writer('</div>\r\n            <div class="alert info">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'infoText'):
            context['self'].infoText(**pageargs)
        

        __M_writer('</div>\r\n            <div class="alert success">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'successText'):
            context['self'].successText(**pageargs)
        

        __M_writer('</div>\r\n            <div class="alert warning">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'warningText'):
            context['self'].warningText(**pageargs)
        

        __M_writer('</div>\r\n        </div>\r\n        <header id="header">\r\n            <nav class="navbar navbar-expand-lg">\r\n                <a href="/"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png" alt="python" /></a>\r\n')
        __M_writer('                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n            </nav>\r\n        </header>\r\n\r\n        <main>\r\n            <div id="site_left">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_right">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

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


def render_dangerText(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def dangerText():
            return render_dangerText(context)
        __M_writer = context.writer()
        __M_writer('This is a danger alert!')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_infoText(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def infoText():
            return render_infoText(context)
        __M_writer = context.writer()
        __M_writer('This is an info alert!')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_successText(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def successText():
            return render_successText(context)
        __M_writer = context.writer()
        __M_writer('This is a succesful alert!')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_warningText(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def warningText():
            return render_warningText(context)
        __M_writer = context.writer()
        __M_writer('This is a warning!')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">\r\n                        <span class="icon-bar"></span>\r\n                        <span class="icon-bar"></span>\r\n                        <span class="icon-bar"></span> \r\n                    </button>\r\n                    <div class="dropdown collapse navbar-collapse" id="myNavbar">        \r\n                        <ul class="nav navbar-nav">\r\n                            <li><a class="dropdown-item nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'index' else ''))
        __M_writer('" href="/">Home</a></li>\r\n                            <li><a class="dropdown-item nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'contact' else ''))
        __M_writer('" href="/homepage/contact">Contact</a></li>\r\n                            <li><a class="dropdown-item nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'about' else ''))
        __M_writer('" href="/homepage/about">About</a></li>\r\n                            <li><a class="dropdown-item nav-link" href="/catalog/index/">Catalog</a></li>\r\n                        </ul>\r\n                        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                            Welcome')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(',' if user.username != '' else ''))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(user.username))
        __M_writer('\r\n                        </button>\r\n                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">\r\n')
        if user.is_authenticated: 
            __M_writer('                                <a class="dropdown-item nav-link" href="/account/logout">Logout</a>\r\n                                <a class="dropdown-item nav-link" href="/catalog/cart">Cart</a>\r\n                                <a class="dropdown-item nav-link" href="/account/preferences">Account</a>\r\n')
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
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n                    <ul class="navbar-nav">\r\n                        <li class="nav-item">\r\n                            <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'index' else ''))
        __M_writer('" href="/homepage/index">Home</a>\r\n                        </li>\r\n                        <li class="nav-item">\r\n                            <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'contact' else ''))
        __M_writer('" href="/homepage/contact">Contact</a>\r\n                        </li>\r\n                        <li class="nav-item">\r\n                            <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == 'about' else ''))
        __M_writer('" href="/homepage/about">About</a>\r\n                        </li>\r\n                        <li class="nav-item">\r\n                            <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('active' if request.dmp.page == '' else ''))
        __M_writer('" href="/catalog/index">Catalog</a>\r\n                        </li>\r\n                    </ul>\r\n                ')
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
        __M_writer('\r\n                    \r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 91, "20": 0, "47": 2, "48": 7, "49": 7, "54": 8, "55": 11, "56": 11, "57": 11, "58": 12, "59": 12, "60": 13, "61": 13, "62": 16, "63": 17, "64": 17, "69": 21, "74": 22, "79": 23, "84": 24, "85": 28, "86": 28, "87": 30, "92": 56, "97": 77, "102": 82, "107": 87, "108": 91, "109": 93, "110": 93, "116": 8, "127": 21, "133": 21, "139": 22, "145": 22, "151": 23, "157": 23, "163": 24, "169": 24, "175": 30, "184": 30, "185": 38, "186": 38, "187": 39, "188": 39, "189": 40, "190": 40, "191": 44, "192": 44, "193": 44, "194": 44, "195": 47, "196": 48, "197": 51, "198": 52, "199": 54, "205": 62, "213": 62, "214": 65, "215": 65, "216": 68, "217": 68, "218": 71, "219": 71, "220": 74, "221": 74, "227": 80, "233": 80, "239": 85, "245": 85, "251": 245}}
__M_END_METADATA
"""
