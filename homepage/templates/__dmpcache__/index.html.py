# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554926609.8987298
_enable_loop = True
_template_filename = 'C:/Users/stick/Developer/Intex/homepage/templates/index.html'
_template_uri = 'index.html'
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
        def site_center():
            return render_site_center(context._locals(__M_locals))
        drugs = context.get('drugs', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        page = context.get('page', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        drugs = context.get('drugs', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        page = context.get('page', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <div class="prescribers">\r\n            <table>\r\n                <tr>\r\n                    <th><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/user.png" alt="user"></th>\r\n                    <th>Name</th>\r\n                    <th>Gender</th>\r\n                    <th>Credentials</th>\r\n                    <th>Location</th>\r\n                    <th>Specialty</th>\r\n                </tr>\r\n')
        for doc in prescribers: 
            __M_writer('                    <tr class="clickable-row" data-href="/detail/prescriber/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(doc[5]))
            __M_writer('/">\r\n                        <td><img src="')
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
        __M_writer('            </table>\r\n        </div>\r\n        <div class="drugs">\r\n            <table>\r\n                <tr>\r\n                    <th><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/pill.png" alt="pill"></th>\r\n                    <th>Name</th>\r\n                    <th>Opioid</th>\r\n                </tr>\r\n')
        for drug in drugs:
            __M_writer('                    <tr class="clickable-row" data-href="/detail/drug/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drug[0]))
            __M_writer('/">\r\n                        <td><img src="')
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


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def site_right():
            return render_site_right(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <form method="post">\r\n        <div class="search">\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_p() ))
        __M_writer('\r\n            <button type="submit" class="searchButton">\r\n                <p class="btn-search">GO</p>\r\n            </button>\r\n        </div>\r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/stick/Developer/Intex/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "46": 1, "51": 3, "56": 51, "61": 62, "67": 3, "73": 3, "79": 4, "90": 4, "91": 9, "92": 9, "93": 17, "94": 18, "95": 18, "96": 18, "97": 19, "98": 19, "99": 20, "100": 20, "101": 21, "102": 21, "103": 22, "104": 22, "105": 23, "106": 23, "107": 24, "108": 24, "109": 27, "110": 32, "111": 32, "112": 37, "113": 38, "114": 38, "115": 38, "116": 39, "117": 39, "118": 40, "119": 40, "120": 41, "121": 41, "122": 44, "123": 47, "124": 47, "125": 47, "126": 47, "127": 48, "128": 48, "134": 53, "142": 53, "143": 56, "144": 56, "150": 144}}
__M_END_METADATA
"""
