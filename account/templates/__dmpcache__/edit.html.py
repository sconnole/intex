# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554991579.7320654
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/account/templates/edit.html'
_template_uri = 'edit.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


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
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        doctor = context.get('doctor', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_center():
            return render_site_center(context)
        self = context.get('self', UNDEFINED)
        doctor = context.get('doctor', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="prescribers">\r\n        <tr>\r\n            <th><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/user.png" alt="user"></th>\r\n            <th>Name</th>\r\n            <th>Gender</th>\r\n            <th>Credentials</th>\r\n            <th>State</th>\r\n            <th>Specialty</th>\r\n        <tr>\r\n        <tr>\r\n            <td><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/user.png" alt="user"></td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[0]))
        __M_writer('</td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[1]))
        __M_writer('</td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[2]))
        __M_writer('</td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[3]))
        __M_writer('</td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[4]))
        __M_writer('</td>\r\n        </tr>\r\n\r\n    </table>\r\n    <form method="post">\r\n        <div class="edit">\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_p() ))
        __M_writer('\r\n            <button type="submit" class="page-btn">\r\n                Update\r\n            </button>\r\n        </div>\r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/account/templates/edit.html", "uri": "edit.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "50": 3, "60": 3, "61": 6, "62": 6, "63": 14, "64": 14, "65": 15, "66": 15, "67": 16, "68": 16, "69": 17, "70": 17, "71": 18, "72": 18, "73": 19, "74": 19, "75": 25, "76": 25, "82": 76}}
__M_END_METADATA
"""
