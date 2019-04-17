# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555084277.9275215
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
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        ratio = context.get('ratio', UNDEFINED)
        avgratio = context.get('avgratio', UNDEFINED)
        docstate = context.get('docstate', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        thisdoc = context.get('thisdoc', UNDEFINED)
        docspecialty = context.get('docspecialty', UNDEFINED)
        docgender = context.get('docgender', UNDEFINED)
        docname = context.get('docname', UNDEFINED)
        specavg = context.get('specavg', UNDEFINED)
        relusers = context.get('relusers', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        doccred = context.get('doccred', UNDEFINED)
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
        thisdoc = context.get('thisdoc', UNDEFINED)
        self = context.get('self', UNDEFINED)
        docspecialty = context.get('docspecialty', UNDEFINED)
        docgender = context.get('docgender', UNDEFINED)
        docname = context.get('docname', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        ratio = context.get('ratio', UNDEFINED)
        avgratio = context.get('avgratio', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def site_center():
            return render_site_center(context)
        docstate = context.get('docstate', UNDEFINED)
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
        __M_writer('%</p>\r\n            <p>of drugs prescribed by this prescriber are opioids</p>\r\n        </div>\r\n        <div class="ratio ratio2">\r\n            <h2>Average Opioid Prescription Ratio</h2>\r\n            <p class="ratio_number">')
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
        def site_right():
            return render_site_right(context)
        specavg = context.get('specavg', UNDEFINED)
        relusers = context.get('relusers', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n        <div class="top_docs">\r\n                <table>\r\n                        <tr>\r\n                            <th>Five Related Prescribers</th>\r\n                        </tr>\r\n')
        for user in relusers:
            __M_writer('                            <tr>\r\n                                <td><a href="/detail/prescriber/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(user[1]))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(user[0]))
            __M_writer('</a></td>\r\n                            </tr>\r\n')
        __M_writer('                    </table>\r\n            <table class="d-info">\r\n                <tr>\r\n                    <th>Prescribed Drug</th>\r\n                    <th>Quantity</th>\r\n                </tr>\r\n')
        for drug in drugs:
            __M_writer('                    <tr>\r\n                        <td><a href="/detail/drug/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[0]))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[0]))
            __M_writer('</a></td>\r\n                        <td class="drug_qty">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[1]))
            __M_writer('</td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n            <table class="a-info">\r\n                <tr>\r\n                    <th>Average</th>\r\n                </tr>\r\n')
        for s in specavg:
            __M_writer('                    <tr>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(s[0]))
            __M_writer('</td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Owner/Google Drive/BYU/2019 1Winter/INTEX/intex/detail/templates/prescriber.html", "uri": "prescriber.html", "source_encoding": "utf-8", "line_map": {"29": 0, "53": 1, "58": 3, "63": 30, "68": 67, "74": 3, "82": 3, "83": 3, "89": 4, "106": 4, "107": 8, "108": 8, "109": 10, "110": 10, "111": 11, "112": 11, "113": 12, "114": 12, "115": 13, "116": 13, "117": 14, "118": 14, "119": 15, "120": 16, "121": 16, "122": 16, "123": 18, "124": 21, "125": 21, "126": 26, "127": 26, "128": 27, "129": 27, "135": 32, "145": 32, "146": 38, "147": 39, "148": 40, "149": 40, "150": 40, "151": 40, "152": 43, "153": 49, "154": 50, "155": 51, "156": 51, "157": 51, "158": 51, "159": 52, "160": 52, "161": 55, "162": 60, "163": 61, "164": 62, "165": 62, "166": 65, "172": 166}}
__M_END_METADATA
"""
