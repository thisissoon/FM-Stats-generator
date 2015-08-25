# Third Party Libs
from xhtml2pdf import pisa
from jinja2 import Environment, PackageLoader
import tempfile


def ms2mins(value):
    return value / (1000 * 60.0)


def ms2hours(value):
    return value / (1000 * 60 * 60.0)


def template_factory(template):
    env = Environment(loader=PackageLoader(__name__, 'templates'))
    env.filters['ms2mins'] = ms2mins
    env.filters['ms2hours'] = ms2hours
    return env.get_template(template)


def html2pdf(content):
    with tempfile.NamedTemporaryFile(delete=False) as fle:
        pisa.CreatePDF(content.encode('utf-8'), fle)
        file_name = fle.name
    return file_name
