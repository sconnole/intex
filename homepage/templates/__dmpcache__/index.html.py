# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554778375.1660063
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'site_center']


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
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

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
        __M_writer('Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="prescribers">\r\n            <table>\r\n                <tr>\r\n                    <th>Icon</th>\r\n                    <th>Name</th>\r\n                    <th>Gender</th>\r\n                    <th>Credentials</th>\r\n                    <th>Location</th>\r\n                    <th>Specialty</th>\r\n                </tr>\r\n')
        for doc in prescribers: 
            __M_writer('                    <tr>\r\n                        <td><img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/user.png" alt="user"></td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[0]))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[1]))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[2]))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[3]))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[4]))
            __M_writer('</td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n        </div>\r\n        <div class="drugs">\r\n            <table>\r\n                <tr>\r\n                    <th>Icon</th>\r\n                    <th>Name</th>\r\n                    <th>Type</th>\r\n                </tr>\r\n')
        for drug in drugs:
            __M_writer('                    <tr>\r\n                        <td><img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/pill.png" alt="pill"></td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[0]))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[1]))
            __M_writer('</td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n        </div> \r\n        <div class="paginate">\r\n            <a class="page-btn ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('hide' if page == 0 else ''))
        __M_writer('" href="/homepage/index/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page-1))
        __M_writer('/">Prev</a>\r\n            <a class="page-btn right" href="/homepage/index/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page+1))
        __M_writer('/">More</a>\r\n        </div>    \r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 3, "53": 51, "59": 3, "65": 3, "71": 4, "82": 4, "83": 17, "84": 18, "85": 19, "86": 19, "87": 20, "88": 20, "89": 21, "90": 21, "91": 22, "92": 22, "93": 23, "94": 23, "95": 24, "96": 24, "97": 27, "98": 37, "99": 38, "100": 39, "101": 39, "102": 40, "103": 40, "104": 41, "105": 41, "106": 44, "107": 47, "108": 47, "109": 47, "110": 47, "111": 48, "112": 48, "118": 112}}
__M_END_METADATA
"""
