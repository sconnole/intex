# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554764149.1871276
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/homepage/templates/index.html'
_template_uri = 'index.html'
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
        self = context.get('self', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        drugs = context.get('drugs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_center():
            return render_site_center(context)
        drugs = context.get('drugs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="prescribers">\r\n            <table>\r\n                <tr>\r\n                    <th>Icon</th>\r\n                    <th>Name</th>\r\n                    <th>Gender</th>\r\n                    <th>Credentials</th>\r\n                    <th>Location</th>\r\n                    <th>Specialty</th>\r\n                </tr>\r\n')
        for doc in prescribers: 
            __M_writer('                    <tr>\r\n                        <td><img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/user.png" alt="user"></td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[0]))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[1]))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[2]))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[3]))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[4]))
            __M_writer('</td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n        </div>\r\n        <div class="drugs">\r\n        <table>\r\n                <tr>\r\n                    <th>Icon</th>\r\n                    <th>Name</th>\r\n                    <th>Type</th>\r\n                </tr>\r\n')
        for drug in drugs:
            __M_writer('                    <tr>\r\n                        <td><img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/pill.png" alt="pill"></td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[0]))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[1]))
            __M_writer('</td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n        </div>     \r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 3, "52": 47, "58": 3, "64": 3, "70": 4, "80": 4, "81": 17, "82": 18, "83": 19, "84": 19, "85": 20, "86": 20, "87": 21, "88": 21, "89": 22, "90": 22, "91": 23, "92": 23, "93": 24, "94": 24, "95": 27, "96": 37, "97": 38, "98": 39, "99": 39, "100": 40, "101": 40, "102": 41, "103": 41, "104": 44, "110": 104}}
__M_END_METADATA
"""
