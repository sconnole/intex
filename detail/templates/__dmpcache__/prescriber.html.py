# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554930750.1122186
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/detail/templates/prescriber.html'
_template_uri = 'prescriber.html'
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
        doccred = context.get('doccred', UNDEFINED)
        docspecialty = context.get('docspecialty', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        docname = context.get('docname', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        docgender = context.get('docgender', UNDEFINED)
        ratio = context.get('ratio', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        docstate = context.get('docstate', UNDEFINED)
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
        docname = context.get('docname', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        doccred = context.get('doccred', UNDEFINED)
        docspecialty = context.get('docspecialty', UNDEFINED)
        docname = context.get('docname', UNDEFINED)
        def site_center():
            return render_site_center(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        docgender = context.get('docgender', UNDEFINED)
        ratio = context.get('ratio', UNDEFINED)
        docstate = context.get('docstate', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="info-card">\r\n            <span class="icon">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/user.png" alt="user">\r\n            </span>\r\n            <h3>Name: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docname))
        __M_writer('</h3>\r\n            <h3>Gender: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docgender))
        __M_writer('</h3>\r\n            <h3>Credentials: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doccred))
        __M_writer('</h3>\r\n            <h3>State: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docstate))
        __M_writer('</h3>\r\n            <h3>Specialty: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docspecialty))
        __M_writer('</h3>\r\n        </div>\r\n        <div class="ratio">\r\n            <h2>Opioid Prescription Ratio</h2>\r\n            <p class="ratio_number">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(ratio))
        __M_writer('%</p>\r\n            <p>of drugs prescribed by this prescriber are opioids</p>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        self = context.get('self', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n        <div class="top_docs">\r\n            <table>\r\n                <tr>\r\n                    <th>Prescribed Drug</th>\r\n                    <th>Quantity</th>\r\n                </tr>\r\n')
        for drug in drugs:
            __M_writer('                    <tr>\r\n                        <td><a href="/detail/drug/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[0]))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[0]))
            __M_writer('</a></td>\r\n                        <td class="drug_qty">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[1]))
            __M_writer('</td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/detail/templates/prescriber.html", "uri": "prescriber.html", "source_encoding": "utf-8", "line_map": {"29": 0, "49": 1, "54": 3, "59": 22, "64": 39, "70": 3, "78": 3, "79": 3, "85": 4, "99": 4, "100": 8, "101": 8, "102": 10, "103": 10, "104": 11, "105": 11, "106": 12, "107": 12, "108": 13, "109": 13, "110": 14, "111": 14, "112": 18, "113": 18, "119": 24, "127": 24, "128": 31, "129": 32, "130": 33, "131": 33, "132": 33, "133": 33, "134": 34, "135": 34, "136": 37, "142": 136}}
__M_END_METADATA
"""
