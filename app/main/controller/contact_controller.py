from flask import request

from flask_restplus import Resource

from ..service.contact_service import (delete_contact, get_all_contacts,
                                       get_contact, get_contact_by_email,
                                       save_new_contact, update_contact)
from ..util.dto import ContactDto

api = ContactDto.api
_contact = ContactDto.contact


@api.route('/')
class ContactList(Resource):
    @api.doc('list_of_contacts')
    @api.marshal_list_with(_contact, envelope='data')
    def get(self):
        """List all contacts"""
        return get_all_contacts()

    @api.expect(_contact, validate=True)
    @api.response(201, 'Contact successfully created.')
    @api.doc('create a new contact')
    def post(self):
        """Creates a new contact """
        data = request.json
        return save_new_contact(data=data)


@api.route('/<username>')
@api.param('username', 'The contact username')
@api.response(404, 'Contact not found.')
class Contact(Resource):
    @api.doc('get a contact by username')
    @api.marshal_with(_contact)
    def get(self, username):
        """get a contact given its username"""
        contact = get_contact(username)
        if not contact:
            api.abort(404)
        else:
            return contact

    @api.doc('update a contact')
    @api.expect(_contact, validate=True)
    @api.marshal_with(_contact)
    def put(self, username):
        """update a contact given its username"""
        data = request.json
        contact, err = update_contact(username, data)
        if not contact:
            api.abort(404, err)
        else:
            return contact

    @api.doc('delete a contact')
    def delete(self, username):
        """delete a contact given its username"""
        contact, err = delete_contact(username)
        if not contact:
            api.abort(404, err)
        else:
            return contact


@api.route('/email/<email>')
@api.param('email', 'The contact email')
@api.response(404, 'Contact not found.')
class ContactByEmail(Resource):
    @api.doc('get a contact by email')
    @api.marshal_with(_contact)
    def get(self, email):
        """get a contact given its email"""
        contact = get_contact_by_email(email)
        if not contact:
            api.abort(404)
        else:
            return contact
