# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555049647.3943
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
        docname = context.get('docname', UNDEFINED)
        docgender = context.get('docgender', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        thisdoc = context.get('thisdoc', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        docstate = context.get('docstate', UNDEFINED)
        relusers = context.get('relusers', UNDEFINED)
        doccred = context.get('doccred', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        docspecialty = context.get('docspecialty', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        ratio = context.get('ratio', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
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
        docname = context.get('docname', UNDEFINED)
        docgender = context.get('docgender', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        thisdoc = context.get('thisdoc', UNDEFINED)
        docstate = context.get('docstate', UNDEFINED)
        doccred = context.get('doccred', UNDEFINED)
        def site_center():
            return render_site_center(context)
        docspecialty = context.get('docspecialty', UNDEFINED)
        ratio = context.get('ratio', UNDEFINED)
        user = context.get('user', UNDEFINED)
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
        __M_writer('</h3>\r\n')
        if user.has_perm('account.change_user'):
            __M_writer('                <a class="page-btn" href="/account/edit/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(thisdoc))
            __M_writer('/">Edit Details</a>\r\n')
        __M_writer('        </div>\r\n        <div class="ratio">\r\n            <h2>Opioid Prescription Ratio</h2>\r\n            <p class="ratio_number">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(ratio))
        __M_writer('%</p>\r\n            <p>of drugs prescribed by this prescriber are opioids</p>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        relusers = context.get('relusers', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
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
{"filename": "C:/Users/Owner/Google Drive/BYU/2019 1Winter/INTEX/intex/detail/templates/prescriber.html", "uri": "prescriber.html", "source_encoding": "utf-8", "line_map": {"29": 0, "51": 1, "56": 3, "61": 25, "66": 52, "72": 3, "80": 3, "81": 3, "87": 4, "103": 4, "104": 8, "105": 8, "106": 10, "107": 10, "108": 11, "109": 11, "110": 12, "111": 12, "112": 13, "113": 13, "114": 14, "115": 14, "116": 15, "117": 16, "118": 16, "119": 16, "120": 18, "121": 21, "122": 21, "128": 27, "137": 27, "138": 33, "139": 34, "140": 35, "141": 35, "142": 35, "143": 35, "144": 38, "145": 44, "146": 45, "147": 46, "148": 46, "149": 46, "150": 46, "151": 47, "152": 47, "153": 50, "159": 153}}
__M_END_METADATA
"""
