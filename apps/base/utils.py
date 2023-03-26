from copy import deepcopy
from datetime import datetime
import os
from rest_framework.permissions import DjangoModelPermissions
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 

def validate_files(request, field, update=False):
    """ 
    :params
    :request: request.data
    :field: key of file    
    """
    
    request = request.copy()

    if update:
        if type(request[field]) == str: request.__delitem__(field)
    else:
        if type(request[field]) == str: request.__setitem__(field, None)        

    return request

def format_date(date):
    date = datetime.strptime(date, '%d/%m/%Y')
    date = f"{date.year}-{date.month}-{date.day}"
    return date

def html_to_pdf(template_src, context_dict={}):
     template = get_template(f"{os.path.abspath(os.path.dirname(__name__))}/{template_src}")
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None
class CustomDjangoModelPermissions(DjangoModelPermissions):

    def __init__(self):
        self.perms_map = deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']