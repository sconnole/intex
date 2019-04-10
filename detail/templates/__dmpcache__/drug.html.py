# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554911224.5784
_enable_loop = True
_template_filename = 'C:/Users/Owner/Google Drive/BYU/2019 1Winter/intex/intex/detail/templates/drug.html'
_template_uri = 'drug.html'
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
        docs = context.get('docs', UNDEFINED)
        drugname = context.get('drugname', UNDEFINED)
        isop = context.get('isop', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
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
        drugname = context.get('drugname', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drugname))
        __M_writer(' Details')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        docs = context.get('docs', UNDEFINED)
        drugname = context.get('drugname', UNDEFINED)
        isop = context.get('isop', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="title_table">\r\n            <table>\r\n                <tr>\r\n                    <td><h1>Drug: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drugname))
        __M_writer('</h1></td>\r\n                </tr>\r\n                <tr>\r\n                    <td><p>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(isop))
        __M_writer('</p></td>\r\n                </tr>\r\n            </table>\r\n        </div>\r\n        <div class="top_docs">\r\n            <h2>Top 10 Prescribers</h2>\r\n            <table>\r\n                <tr>\r\n                    <th>Name</th>\r\n                </tr>\r\n')
        for doc in docs:
            __M_writer('                    <tr>\r\n                        <td><a href="/detail/prescriber/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[1]))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[0]))
            __M_writer('</a></td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n        </div>   \r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Owner/Google Drive/BYU/2019 1Winter/intex/intex/detail/templates/drug.html", "uri": "drug.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 3, "52": 30, "58": 3, "66": 3, "67": 3, "73": 4, "83": 4, "84": 9, "85": 9, "86": 12, "87": 12, "88": 22, "89": 23, "90": 24, "91": 24, "92": 24, "93": 24, "94": 27, "100": 94}}
__M_END_METADATA
"""
