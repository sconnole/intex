# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550078674.3622122
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/mysite/account/templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'site_center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Login')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <p>Dolor voluptate aliqua do sunt est eiusmod commodo nisi quis. Officia ipsum nostrud voluptate aute do id. Irure sint nulla id sit qui laborum tempor consectetur magna incididunt nisi deserunt laboris nostrud. Veniam dolore sunt Lorem aliqua velit consequat officia excepteur nisi tempor et velit incididunt ad.</p>\r\n    <p>Qui voluptate ea excepteur exercitation cillum ad mollit in anim labore enim amet tempor. Est consequat exercitation pariatur laboris eiusmod tempor. Voluptate eiusmod do ut Lorem qui. Deserunt eiusmod do veniam fugiat. Eu qui laboris cupidatat consequat irure Lorem nulla proident Lorem aute commodo. Nostrud esse laboris Lorem in laborum non laborum amet.</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/mysite/account/templates/login.html", "uri": "login.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 3, "53": 3, "59": 3, "65": 4, "71": 4, "77": 71}}
__M_END_METADATA
"""
