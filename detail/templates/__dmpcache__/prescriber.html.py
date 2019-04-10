# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554918876.233123
_enable_loop = True
_template_filename = 'C:/Users/Owner/Google Drive/BYU/2019 1Winter/intex/intex/detail/templates/prescriber.html'
_template_uri = 'prescriber.html'
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
        self = context.get('self', UNDEFINED)
        docname = context.get('docname', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        doccred = context.get('doccred', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        ratio = context.get('ratio', UNDEFINED)
        docgender = context.get('docgender', UNDEFINED)
        docspecialty = context.get('docspecialty', UNDEFINED)
        docstate = context.get('docstate', UNDEFINED)
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
        self = context.get('self', UNDEFINED)
        docname = context.get('docname', UNDEFINED)
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docname))
        __M_writer(' Details')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        docname = context.get('docname', UNDEFINED)
        doccred = context.get('doccred', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        ratio = context.get('ratio', UNDEFINED)
        docgender = context.get('docgender', UNDEFINED)
        docspecialty = context.get('docspecialty', UNDEFINED)
        docstate = context.get('docstate', UNDEFINED)
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="title_table">\r\n            <table>\r\n                <tr>\r\n                    <td><h1>Name: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docname))
        __M_writer('</h1></td>\r\n                    <td><p>Credentials: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doccred))
        __M_writer('</p></td>\r\n                </tr>\r\n                <tr>\r\n                    <td><p>Gender: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docgender))
        __M_writer('</p></td>\r\n                    <td><p>State: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docstate))
        __M_writer('</p></td>\r\n                </tr>\r\n                <tr>\r\n                    <td><p>Specialty: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docspecialty))
        __M_writer('</p></td>\r\n                </tr>\r\n            </table>\r\n        </div>\r\n        <div class="top_docs">\r\n            <h2>Drugs Prescribed</h2>\r\n            <table>\r\n                <tr>\r\n                    <th>Drug Name</th>\r\n                    <th>Quantity</th>\r\n                </tr>\r\n')
        for drug in drugs:
            __M_writer('                    <tr>\r\n                        <td><a href="/detail/drug/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[0]))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[0]))
            __M_writer('</a></td>\r\n                        <td class="drug_qty">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[1]))
            __M_writer('</td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n        </div>\r\n        <div class="ratio">\r\n            <h2>Opioid Prescription Ratio</h2>\r\n            <p class="ratio_number">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(ratio))
        __M_writer('%</p>\r\n            <p>of drugs prescribed by this prescriber are opioids</p>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Owner/Google Drive/BYU/2019 1Winter/intex/intex/detail/templates/prescriber.html", "uri": "prescriber.html", "source_encoding": "utf-8", "line_map": {"29": 0, "46": 1, "51": 3, "56": 42, "62": 3, "70": 3, "71": 3, "77": 4, "91": 4, "92": 9, "93": 9, "94": 10, "95": 10, "96": 13, "97": 13, "98": 14, "99": 14, "100": 17, "101": 17, "102": 28, "103": 29, "104": 30, "105": 30, "106": 30, "107": 30, "108": 31, "109": 31, "110": 34, "111": 38, "112": 38, "118": 112}}
__M_END_METADATA
"""
