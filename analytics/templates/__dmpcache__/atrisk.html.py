# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554950946.336687
_enable_loop = True
_template_filename = 'C:/Users/majohnso/Desktop/intex/analytics/templates/atrisk.html'
_template_uri = 'atrisk.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


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
        docs = context.get('docs', UNDEFINED)
        page = context.get('page', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        docs = context.get('docs', UNDEFINED)
        page = context.get('page', UNDEFINED)
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div>  \r\n<h1>Drugs often Perscribed with opioids: </h1>\r\n\r\n    <ul>\r\n        <li>TRAMADOL_HCL</li>\r\n        <li>CEPHALEXIN</li>\r\n        <li>LEVOFLOXACIN</li>\r\n        <li>GABAPENTIN</li>\r\n        <li>METFORMIN_HCL</li>\r\n        <li>SULFAMETHOXAZOLE_TRIMETHOOPRIM</li>\r\n        <li>HYDROCHLOROTHAZIDE</li>\r\n\r\n      </ul>\r\n</div> \r\n\r\n<h1> Providers who are at risk of Perscribing opioids: </h1>\r\n\r\n<div>\r\n    <table>\r\n        <tr>\r\n            <th>Name</th>\r\n            <th>TRAMADOL_HCL</th>\r\n            <th>CEPHALEXIN</th>\r\n            <th>LEVOFLOXACIN</th>\r\n            <th>GABAPENTIN</th>\r\n            <th>METFORMIN_HCL</th>\r\n            <th>SULFAMETHOXAZOLE_TRIMETHOOPRIM</th>\r\n            <th>HYDROCHLOROTHAZIDE</th>\r\n        </tr>\r\n')
        for doc in docs: 
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[0]))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[1]))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[2]))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[3]))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[4]))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[5]))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[6]))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n    <div class="paginate">\r\n        <a class="page-btn ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('hide' if page == 0 else ''))
        __M_writer('" href="/analytics/atRisk">Prev</a>\r\n        <a class="page-btn right" href="/analytics/atRisk">More</a>\r\n    </div>\r\n    </div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/majohnso/Desktop/intex/analytics/templates/atrisk.html", "uri": "atrisk.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "44": 53, "50": 3, "59": 3, "60": 34, "61": 35, "62": 36, "63": 36, "64": 37, "65": 37, "66": 38, "67": 38, "68": 39, "69": 39, "70": 40, "71": 40, "72": 41, "73": 41, "74": 42, "75": 42, "76": 45, "77": 47, "78": 47, "84": 78}}
__M_END_METADATA
"""
