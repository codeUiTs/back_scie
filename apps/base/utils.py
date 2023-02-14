from copy import deepcopy
from datetime import datetime
from rest_framework.permissions import DjangoModelPermissions

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

class CustomDjangoModelPermissions(DjangoModelPermissions):

    def __init__(self):
        self.perms_map = deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']