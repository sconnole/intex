# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555041347.836239
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/analytics/templates/risk.html'
_template_uri = 'risk.html'
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
        self = context.get('self', UNDEFINED)
        page = context.get('page', UNDEFINED)
        docs = context.get('docs', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
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
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('At-Risk')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        page = context.get('page', UNDEFINED)
        def site_center():
            return render_site_center(context)
        self = context.get('self', UNDEFINED)
        docs = context.get('docs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div>\r\n    <table class="prescribers">\r\n        <tr>\r\n            <th>Name</th>\r\n            <th>TRAMADOL_HCL</th>\r\n            <th>CEPHALEXIN</th>\r\n            <th>LEVOFLOXACIN</th>\r\n            <th>GABAPENTIN</th>\r\n            <th>METFORMIN_HCL</th>\r\n            <th>SULFAMETHOXAZOLE_TRIMETHOOPRIM</th>\r\n            <th>HYDROCHLOROTHAZIDE</th>\r\n            <th>Total Prescriptions</th>\r\n            <th>At Risk Score</th>\r\n        </tr>\r\n')
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
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[7]))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[8]))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[9]))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n    <div class="paginate">\r\n        <a class="page-btn ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('hide' if page == 0 else ''))
        __M_writer('" href="/analytics/risk/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page-1))
        __M_writer('/">Prev</a>\r\n        <a class="page-btn right" href="/analytics/risk/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page+1))
        __M_writer('/">More</a>\r\n    </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <p>Drugs prescribed with opioids: </p>\r\n        <ul>\r\n            <li>TRAMADOL_HCL</li>\r\n            <li>CEPHALEXIN</li>\r\n            <li>LEVOFLOXACIN</li>\r\n            <li>GABAPENTIN</li>\r\n            <li>METFORMIN_HCL</li>\r\n            <li>SULFAMETHOXAZOLE_TRIMETHOOPRIM</li>\r\n            <li>HYDROCHLOROTHAZIDE</li>\r\n        </ul>\r\n    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/analytics/templates/risk.html", "uri": "risk.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 3, "53": 40, "58": 54, "64": 3, "70": 3, "76": 5, "85": 5, "86": 20, "87": 21, "88": 22, "89": 22, "90": 23, "91": 23, "92": 24, "93": 24, "94": 25, "95": 25, "96": 26, "97": 26, "98": 27, "99": 27, "100": 28, "101": 28, "102": 29, "103": 29, "104": 30, "105": 30, "106": 31, "107": 31, "108": 34, "109": 36, "110": 36, "111": 36, "112": 36, "113": 37, "114": 37, "120": 42, "126": 42, "132": 126}}
__M_END_METADATA
"""
