
from flask_restplus import Namespace, fields


class ContactDto:
    api = Namespace('contact', description='contact related operations')
    contact = api.model('contact', {
        'emails': fields.List(fields.String(attribute='email'),
                              attribute='email', required=True, description='contact email addresses'),
        'username': fields.String(required=True, description='username'),
        'first_name': fields.String(required=True, description='first name'),
        'surname': fields.String(required=True, description='surname')
    })
