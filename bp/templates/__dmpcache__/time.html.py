# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555619613.0721977
_enable_loop = True
_template_filename = 'C:/Users/Owner/Google Drive/BYU/2019 1Winter/INTEX/intex/bp/templates/time.html'
_template_uri = 'time.html'
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        days = context.get('days', UNDEFINED)
        years = context.get('years', UNDEFINED)
        months = context.get('months', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        days = context.get('days', UNDEFINED)
        years = context.get('years', UNDEFINED)
        months = context.get('months', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h1>Days as Client Predictor</h1>\r\n    <div class="form-content">\r\n        <form method="post">\r\n            <table>\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_p() ))
        __M_writer('\r\n            </table>\r\n            <input class="main-btn" type="submit" value="Predict">\r\n        </form>\r\n    </div>\r\n')
        if request.method == 'POST':
            __M_writer('        <div class="result">\r\n            <h2>A client with these attributes is predicted to stay with BP for:</h2>\r\n            <p>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( days ))
            __M_writer(' days</p>\r\n            <p>Or ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( years ))
            __M_writer(' years, ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( months ))
            __M_writer(' months</p>\r\n        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Owner/Google Drive/BYU/2019 1Winter/INTEX/intex/bp/templates/time.html", "uri": "time.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "52": 3, "64": 3, "65": 8, "66": 8, "67": 13, "68": 14, "69": 16, "70": 16, "71": 17, "72": 17, "73": 17, "74": 17, "80": 74}}
__M_END_METADATA
"""
