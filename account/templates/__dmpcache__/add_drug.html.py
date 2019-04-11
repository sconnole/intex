# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555020251.106695
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/account/templates/add_drug.html'
_template_uri = 'add_drug.html'
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
        dropdown = context.get('dropdown', UNDEFINED)
        doctorID = context.get('doctorID', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        current_drugs = context.get('current_drugs', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        doctor = context.get('doctor', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Manage Drugs')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        dropdown = context.get('dropdown', UNDEFINED)
        doctorID = context.get('doctorID', UNDEFINED)
        current_drugs = context.get('current_drugs', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
        doctor = context.get('doctor', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h1>Prescriptions by: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctor[0]))
        __M_writer('</h1>\r\n    <form action = "/account/add_drug/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doctorID))
        __M_writer('" method = "POST"> \r\n        <select name ="drug">\r\n')
        for item in dropdown: 
            __M_writer('                <option value=')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item[0]))
            __M_writer('>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item[0]))
            __M_writer('</option>\r\n')
        __M_writer('        </select>\r\n        <label for="quanity">Quantity</label>\r\n        <input type="number" name="quantity" value="1" step="5"/>    \r\n        <button type="submit" class="page-btn">\r\n            Add\r\n        </button>\r\n    </form>\r\n    <table class="prescribers">\r\n        <tr>\r\n            <th>Name</th>\r\n            <th>Quantity</th>\r\n        </tr>\r\n')
        for drug in current_drugs:
            __M_writer('            <tr>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[0]))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[1]))
            __M_writer('</td>\r\n            <tr>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/account/templates/add_drug.html", "uri": "add_drug.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 3, "58": 3, "64": 3, "70": 5, "81": 5, "82": 6, "83": 6, "84": 7, "85": 7, "86": 9, "87": 10, "88": 10, "89": 10, "90": 10, "91": 10, "92": 12, "93": 24, "94": 25, "95": 26, "96": 26, "97": 27, "98": 27, "104": 98}}
__M_END_METADATA
"""
