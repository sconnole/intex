# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555646136.2483056
_enable_loop = True
_template_filename = 'C:/Users/Owner/Google Drive/BYU/2019 1Winter/INTEX/intex/bp/templates/newdata.html'
_template_uri = 'newdata.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        success = context.get('success', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        success = context.get('success', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h1>Add Client Record</h1>\r\n    <div class="wrapper">\r\n        <div class="form-content form-style-5">\r\n            <form method="post">\r\n                <table>\r\n                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_p() ))
        __M_writer('\r\n                </table>\r\n                <input class="main-btn" type="submit" value="Add Client Record">\r\n            </form>\r\n        </div>\r\n')
        if request.method == 'POST':
            __M_writer('            <div class="result">\r\n                <h2>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( success ))
            __M_writer('</h2>\r\n            </div>\r\n')
        __M_writer('    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Owner/Google Drive/BYU/2019 1Winter/INTEX/intex/bp/templates/newdata.html", "uri": "newdata.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "50": 3, "60": 3, "61": 9, "62": 9, "63": 14, "64": 15, "65": 16, "66": 16, "67": 19, "73": 67}}
__M_END_METADATA
"""
