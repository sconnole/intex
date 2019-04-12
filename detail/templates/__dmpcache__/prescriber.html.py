# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555038146.2549827
_enable_loop = True
_template_filename = 'C:/Users/Owner/Google Drive/BYU/2019 1Winter/INTEX/intex/detail/templates/prescriber.html'
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
        docgender = context.get('docgender', UNDEFINED)
        docstate = context.get('docstate', UNDEFINED)
        relusers = context.get('relusers', UNDEFINED)
        doccred = context.get('doccred', UNDEFINED)
        docname = context.get('docname', UNDEFINED)
        ratio = context.get('ratio', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        drugs = context.get('drugs', UNDEFINED)
        docspecialty = context.get('docspecialty', UNDEFINED)
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
        def title():
            return render_title(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docname))
        __M_writer(' Details')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        docgender = context.get('docgender', UNDEFINED)
        docstate = context.get('docstate', UNDEFINED)
        doccred = context.get('doccred', UNDEFINED)
        docname = context.get('docname', UNDEFINED)
        ratio = context.get('ratio', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        docspecialty = context.get('docspecialty', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
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
        drugs = context.get('drugs', UNDEFINED)
        relusers = context.get('relusers', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <div class="top_docs">\r\n                <table>\r\n                        <tr>\r\n                            <th>Five Related Prescribers</th>\r\n                        </tr>\r\n')
        for user in relusers:
            __M_writer('                            <tr>\r\n                                <td><a href="/detail/prescriber/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(user[1]))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(user[0]))
            __M_writer('</a></td>\r\n                            </tr>\r\n')
        __M_writer('                    </table>\r\n            <table>\r\n                <tr>\r\n                    <th>Prescribed Drug</th>\r\n                    <th>Quantity</th>\r\n                </tr>\r\n')
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
{"filename": "C:/Users/Owner/Google Drive/BYU/2019 1Winter/INTEX/intex/detail/templates/prescriber.html", "uri": "prescriber.html", "source_encoding": "utf-8", "line_map": {"29": 0, "50": 1, "55": 3, "60": 22, "65": 49, "71": 3, "79": 3, "80": 3, "86": 4, "100": 4, "101": 8, "102": 8, "103": 10, "104": 10, "105": 11, "106": 11, "107": 12, "108": 12, "109": 13, "110": 13, "111": 14, "112": 14, "113": 18, "114": 18, "120": 24, "129": 24, "130": 30, "131": 31, "132": 32, "133": 32, "134": 32, "135": 32, "136": 35, "137": 41, "138": 42, "139": 43, "140": 43, "141": 43, "142": 43, "143": 44, "144": 44, "145": 47, "151": 145}}
__M_END_METADATA
"""
