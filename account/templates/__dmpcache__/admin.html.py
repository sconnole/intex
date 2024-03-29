# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555082506.864015
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/account/templates/admin.html'
_template_uri = 'admin.html'
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
        docs = context.get('docs', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        page = context.get('page', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        docs = context.get('docs', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        page = context.get('page', UNDEFINED)
        def site_center():
            return render_site_center(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n     <div class="content">\r\n        <div class="prescribers">\r\n            <table>\r\n                <tr>\r\n                    <th><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/user.png" alt="user"></th>\r\n                    <th>First Name</th>\r\n                    <th>Last Name</th>\r\n                    <th>&nbsp;</th>\r\n                    <th>&nbsp;</th>\r\n                    <th>&nbsp;</th>\r\n                </tr>\r\n')
        for doc in docs: 
            __M_writer('                    <tr>\r\n                        <td><img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/user.png" alt="user"></td>\r\n                        <td><a class="list_link" href="/detail/prescriber/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[2]))
            __M_writer('/">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[0]))
            __M_writer('</a></td>\r\n                        <td><a class="list_link" href="/detail/prescriber/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[2]))
            __M_writer('/">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[1]))
            __M_writer('</a></td>\r\n                        <td><a class="page-btn" href="/account/edit/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[2]))
            __M_writer('/">Edit</a></td>\r\n                        <td><a class="page-btn" href="/account/delete/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[2]))
            __M_writer('/">Delete</a></td>\r\n                        <td><a class="page-btn" href="/account/add_drug/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[2]))
            __M_writer('/">Add Drug</a></td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n        </div>\r\n        <div class="paginate">\r\n            <a class="page-btn ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('hide' if page == 0 else ''))
        __M_writer('" href="/account/admin/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page-1))
        __M_writer('/">Prev</a>\r\n            <a class="page-btn right" href="/account/admin/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page+1))
        __M_writer('/">More</a>\r\n        </div>  \r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <form method="post">\r\n        <div class="search">\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_p() ))
        __M_writer('\r\n            <button type="submit" class="searchButton">\r\n                <p class="btn-search">GO</p>\r\n            </button>\r\n        </div>\r\n    </form>\r\n    <a href=\'/account/add/\' class="main-btn">Add New Prescriber</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/account/templates/admin.html", "uri": "admin.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 32, "53": 44, "59": 3, "69": 3, "70": 8, "71": 8, "72": 15, "73": 16, "74": 17, "75": 17, "76": 18, "77": 18, "78": 18, "79": 18, "80": 19, "81": 19, "82": 19, "83": 19, "84": 20, "85": 20, "86": 21, "87": 21, "88": 22, "89": 22, "90": 25, "91": 28, "92": 28, "93": 28, "94": 28, "95": 29, "96": 29, "102": 34, "110": 34, "111": 37, "112": 37, "118": 112}}
__M_END_METADATA
"""
