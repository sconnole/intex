# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554932338.98184
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/detail/templates/drug.html'
_template_uri = 'drug.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'site_center', 'site_right']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        drugname = context.get('drugname', UNDEFINED)
        isop = context.get('isop', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        docs = context.get('docs', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context)
        drugname = context.get('drugname', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drugname))
        __M_writer(' Details')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_center():
            return render_site_center(context)
        drugname = context.get('drugname', UNDEFINED)
        isop = context.get('isop', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="info-card">\r\n            <span class="icon">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/pill.png" alt="pill">\r\n            </span>\r\n            <h3>Drug: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drugname))
        __M_writer('</h3>\r\n            <h3>Opiod: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(isop))
        __M_writer('</h3>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        self = context.get('self', UNDEFINED)
        docs = context.get('docs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="top_docs">\r\n        <table>\r\n            <tr>\r\n                <th>Top Ten Prescribers</th>\r\n            </tr>\r\n')
        for doc in docs:
            __M_writer('                <tr>\r\n                    <td><a href="/detail/prescriber/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[1]))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[0]))
            __M_writer('</a></td>\r\n                </tr>\r\n')
        __M_writer('        </table>\r\n    </div> \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/detail/templates/drug.html", "uri": "drug.html", "source_encoding": "utf-8", "line_map": {"29": 0, "45": 1, "50": 3, "55": 14, "60": 29, "66": 3, "74": 3, "75": 3, "81": 4, "91": 4, "92": 8, "93": 8, "94": 10, "95": 10, "96": 11, "97": 11, "103": 16, "111": 16, "112": 22, "113": 23, "114": 24, "115": 24, "116": 24, "117": 24, "118": 27, "124": 118}}
__M_END_METADATA
"""
