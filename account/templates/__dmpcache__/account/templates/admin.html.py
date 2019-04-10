# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554925640.9696114
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/account/templates/admin.html'
_template_uri = '/account/templates/admin.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_right']


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
        form = context.get('form', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
{"filename": "C:/Users/stick/Developer/Intex/account/templates/admin.html", "uri": "/account/templates/admin.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 13, "49": 3, "57": 3, "58": 6, "59": 6, "65": 59}}
__M_END_METADATA
"""
