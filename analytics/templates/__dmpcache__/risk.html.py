# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555013020.8780515
_enable_loop = True
_template_filename = 'C:/Users/majohnso/Desktop/intex/analytics/templates/risk.html'
_template_uri = 'risk.html'
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
        def site_center():
            return render_site_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        docs = context.get('docs', UNDEFINED)
        page = context.get('page', UNDEFINED)
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
        def site_center():
            return render_site_center(context)
        self = context.get('self', UNDEFINED)
        docs = context.get('docs', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div>  \r\n<h1>Drugs often Perscribed with opioids: </h1>\r\n\r\n    <ul>\r\n        <li>TRAMADOL_HCL</li>\r\n        <li>CEPHALEXIN</li>\r\n        <li>LEVOFLOXACIN</li>\r\n        <li>GABAPENTIN</li>\r\n        <li>METFORMIN_HCL</li>\r\n        <li>SULFAMETHOXAZOLE_TRIMETHOOPRIM</li>\r\n        <li>HYDROCHLOROTHAZIDE</li>\r\n\r\n      </ul>\r\n</div> \r\n\r\n<h1> Providers who are at risk of Perscribing opioids: </h1>\r\n\r\n<div>\r\n    <table>\r\n        <tr>\r\n            <th>Name</th>\r\n            <th>TRAMADOL_HCL</th>\r\n            <th>CEPHALEXIN</th>\r\n            <th>LEVOFLOXACIN</th>\r\n            <th>GABAPENTIN</th>\r\n            <th>METFORMIN_HCL</th>\r\n            <th>SULFAMETHOXAZOLE_TRIMETHOOPRIM</th>\r\n            <th>HYDROCHLOROTHAZIDE</th>\r\n        </tr>\r\n')
        for doc in docs: 
            __M_writer('            \r\n            <tr>\r\n                <td>')
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
        __M_writer('" href="/analytics/risk/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page-1))
        __M_writer('/">Prev</a>\r\n        <a class="page-btn right" href="/analytics/risk/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page+1))
        __M_writer('/">More</a>\r\n    </div>\r\n    </div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/majohnso/Desktop/intex/analytics/templates/risk.html", "uri": "risk.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "44": 54, "50": 3, "59": 3, "60": 34, "61": 35, "62": 37, "63": 37, "64": 38, "65": 38, "66": 39, "67": 39, "68": 40, "69": 40, "70": 41, "71": 41, "72": 42, "73": 42, "74": 43, "75": 43, "76": 46, "77": 48, "78": 48, "79": 48, "80": 48, "81": 49, "82": 49, "88": 82}}
__M_END_METADATA
"""
