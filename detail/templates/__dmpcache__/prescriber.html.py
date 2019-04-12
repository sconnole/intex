# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555077072.5126145
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        docstate = context.get('docstate', UNDEFINED)
        docgender = context.get('docgender', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        avgratio = context.get('avgratio', UNDEFINED)
        docspecialty = context.get('docspecialty', UNDEFINED)
        docname = context.get('docname', UNDEFINED)
        ratio = context.get('ratio', UNDEFINED)
        thisdoc = context.get('thisdoc', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        doccred = context.get('doccred', UNDEFINED)
        relusers = context.get('relusers', UNDEFINED)
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
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context)
        docname = context.get('docname', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docname))
        __M_writer(' Details')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        docstate = context.get('docstate', UNDEFINED)
        docgender = context.get('docgender', UNDEFINED)
        avgratio = context.get('avgratio', UNDEFINED)
        def site_center():
            return render_site_center(context)
        docspecialty = context.get('docspecialty', UNDEFINED)
        docname = context.get('docname', UNDEFINED)
        ratio = context.get('ratio', UNDEFINED)
        user = context.get('user', UNDEFINED)
        thisdoc = context.get('thisdoc', UNDEFINED)
        self = context.get('self', UNDEFINED)
        doccred = context.get('doccred', UNDEFINED)
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
        __M_writer('%</p>\r\n            <p>of drugs prescribed by this prescriber are opioids</p>\r\n        </div>\r\n        <div class="ratio">\r\n            <h2>Average Opioid Prescription Ratio</h2>\r\n            <p class="ratio_number">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(avgratio))
        __M_writer('%</p>\r\n            <p>of drugs prescribed by prescribers specializing in ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(docspecialty))
        __M_writer(' are opioids</p>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        relusers = context.get('relusers', UNDEFINED)
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
{"filename": "C:/Users/Owner/Google Drive/BYU/2019 1Winter/INTEX/intex/detail/templates/prescriber.html", "uri": "prescriber.html", "source_encoding": "utf-8", "line_map": {"29": 0, "52": 1, "57": 3, "62": 30, "67": 57, "73": 3, "81": 3, "82": 3, "88": 4, "105": 4, "106": 8, "107": 8, "108": 10, "109": 10, "110": 11, "111": 11, "112": 12, "113": 12, "114": 13, "115": 13, "116": 14, "117": 14, "118": 15, "119": 16, "120": 16, "121": 16, "122": 18, "123": 21, "124": 21, "125": 26, "126": 26, "127": 27, "128": 27, "134": 32, "143": 32, "144": 38, "145": 39, "146": 40, "147": 40, "148": 40, "149": 40, "150": 43, "151": 49, "152": 50, "153": 51, "154": 51, "155": 51, "156": 51, "157": 52, "158": 52, "159": 55, "165": 159}}
__M_END_METADATA
"""
