# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555011366.2619786
_enable_loop = True
_template_filename = 'C:/Users/majohnso/Desktop/intex/analytics/templates/index.html'
_template_uri = 'index.html'
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
        related = context.get('related', UNDEFINED)
        page = context.get('page', UNDEFINED)
        dropdown = context.get('dropdown', UNDEFINED)
        self = context.get('self', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
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
        related = context.get('related', UNDEFINED)
        page = context.get('page', UNDEFINED)
        dropdown = context.get('dropdown', UNDEFINED)
        self = context.get('self', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    \r\n<h1>Unethical Perscribers: </h1>\r\n\r\n<div class="prescribers">\r\n    <table>\r\n        <tr>\r\n            <th>Name</th>\r\n            <th>Specialty</th>\r\n            <th>Opioid perscription ratio</th>\r\n        </tr>\r\n')
        for doc in prescribers: 
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[0]))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[1]))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[2]))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n    <div class="paginate">\r\n        <a class="page-btn ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('hide' if page == 0 else ''))
        __M_writer('" href="/analytics/index">Prev</a>\r\n        <a class="page-btn right" href="/analytics/index">More</a>\r\n    </div> \r\n\r\n   \r\n</div>\r\n\r\n<div> \r\n    <br>\r\n    <br>\r\n    <form action = "index" method = "POST"> \r\n    <h2>Find similar potential Unethical Perscribers: </h2>\r\n    <select name ="doctorID">\r\n')
        for item in dropdown: 
            __M_writer('                <option value=')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item[1]))
            __M_writer('>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item[0]))
            __M_writer('</option>\r\n')
        __M_writer('    </select>\r\n    <button type="submit" class="page-btn">\r\n            Submit\r\n        </button>\r\n</form>\r\n\r\n\r\n</div>\r\n')
        for item in related:
            __M_writer('    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item[0]))
            __M_writer('</td>\r\n')
        __M_writer('\r\n<div>\r\n    \r\n\r\n</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/majohnso/Desktop/intex/analytics/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 59, "52": 3, "63": 3, "64": 15, "65": 16, "66": 17, "67": 17, "68": 18, "69": 18, "70": 19, "71": 19, "72": 22, "73": 24, "74": 24, "75": 37, "76": 38, "77": 38, "78": 38, "79": 38, "80": 38, "81": 40, "82": 48, "83": 49, "84": 49, "85": 49, "86": 51, "92": 86}}
__M_END_METADATA
"""
