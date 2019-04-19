# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555647639.9125724
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
        form = context.get('form', UNDEFINED)
        days = context.get('days', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        months = context.get('months', UNDEFINED)
        self = context.get('self', UNDEFINED)
        years = context.get('years', UNDEFINED)
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
        days = context.get('days', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        months = context.get('months', UNDEFINED)
        self = context.get('self', UNDEFINED)
        years = context.get('years', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h1>Days as Client Predictor</h1>\r\n    <div class="wrapper">\r\n        <div class="form-content form-style-5">\r\n            <form method="post">\r\n                <table>\r\n                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_p() ))
        __M_writer('\r\n                </table>\r\n                <input class="main-btn" type="submit" value="Predict">\r\n            </form>\r\n        </div>\r\n')
        if request.method == 'POST':
            __M_writer('            <div class="result">\r\n                <h2>A client with these attributes is predicted to stay with BP for:</h2>\r\n                <p>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( days ))
            __M_writer(' days</p>\r\n                <p>Or ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( years ))
            __M_writer(' years, ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( months ))
            __M_writer(' months</p>\r\n            </div>\r\n')
        __M_writer("    </div>\r\n    <div class='tableauPlaceholder' id='viz1555641633927' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;8X&#47;8X63B58YX&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;8X63B58YX' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;8X&#47;8X63B58YX&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='filter' value='publish=yes' /></object></div>\r\n    <script type='text/javascript'>\r\n        var divElement = document.getElementById('viz1555641633927');\r\n        var vizElement = divElement.getElementsByTagName('object')[0];\r\n        vizElement.style.width='1016px';\r\n        vizElement.style.height='991px';\r\n        var scriptElement = document.createElement('script');\r\n        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';\r\n        vizElement.parentNode.insertBefore(scriptElement, vizElement);\r\n    </script>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Owner/Google Drive/BYU/2019 1Winter/INTEX/intex/bp/templates/time.html", "uri": "time.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "52": 3, "64": 3, "65": 9, "66": 9, "67": 14, "68": 15, "69": 17, "70": 17, "71": 18, "72": 18, "73": 18, "74": 18, "75": 21, "81": 75}}
__M_END_METADATA
"""
