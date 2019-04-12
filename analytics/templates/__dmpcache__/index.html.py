# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555040589.2852762
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/analytics/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center', 'site_right']


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
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        page = context.get('page', UNDEFINED)
        self = context.get('self', UNDEFINED)
        dropdown = context.get('dropdown', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        related = context.get('related', UNDEFINED)
        __M_writer = context.writer()
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


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        def site_center():
            return render_site_center(context)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="prescribers">\r\n        <table>\r\n            <tr>\r\n                <th>Name</th>\r\n                <th>Specialty</th>\r\n                <th>Opioid prescription ratio</th>\r\n            </tr>\r\n')
        for doc in prescribers: 
            __M_writer('                <tr>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[0]))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[1]))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[2]))
            __M_writer('</td>\r\n                </tr>\r\n')
        __M_writer('        </table>\r\n        <div class="paginate">\r\n            <a class="page-btn ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('hide' if page == 0 else ''))
        __M_writer('" href="/analytics/index">Prev</a>\r\n            <a class="page-btn right" href="/analytics/index">More</a>\r\n        </div> \r\n    </div>\r\n    <div> \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        related = context.get('related', UNDEFINED)
        dropdown = context.get('dropdown', UNDEFINED)
        def site_right():
            return render_site_right(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <form class="similar" method= "POST"> \r\n        <p>Find Similar to: </p>\r\n            <select name ="doctorID">\r\n')
        for item in dropdown: 
            __M_writer('                    <option value=')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item[1]))
            __M_writer('>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item[0]))
            __M_writer('</option>\r\n')
        __M_writer('            </select>\r\n        <button type="submit" class="page-btn">Submit</button>\r\n    </form> \r\n    <table class="similar">\r\n        <tr>\r\n            <th>Name</th>\r\n        </tr>\r\n')
        for item in related:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item[0]))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/analytics/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 25, "53": 47, "59": 3, "68": 3, "69": 11, "70": 12, "71": 13, "72": 13, "73": 14, "74": 14, "75": 15, "76": 15, "77": 18, "78": 20, "79": 20, "85": 27, "94": 27, "95": 31, "96": 32, "97": 32, "98": 32, "99": 32, "100": 32, "101": 34, "102": 41, "103": 42, "104": 43, "105": 43, "106": 46, "112": 106}}
__M_END_METADATA
"""
