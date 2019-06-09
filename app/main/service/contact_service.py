from app.main import db
from app.main.model.contact import Contact
from app.main.model.email import Email

import uuid


def save_new_contact(data):
    """ creates Contact in db """
    contact = Contact.query.filter_by(username=data['username']).first()
    if not contact:
        new_contact = Contact(
            username=data['username'],
            first_name=data['first_name'],
            surname=data['surname']
        )
        for email in data['emails']:
            new_contact.email.append(Email(email=email))
        save_changes(new_contact)
        response_object = {
            'status': 'success',
            'message': 'Contact successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Contact already exists.',
        }
        return response_object, 409


def get_all_contacts():
    """ returns all contacts from db"""
    return Contact.query.all()


def get_contact(username):
    """ returns a contact by username"""
    return Contact.query.filter_by(username=username).first()


def get_contact_by_email(email):
    """ returns a contact by email"""
    return Contact.query.join(Contact.email, aliased=True).filter_by(email=email).first()


def update_contact(username, data):
    contact = Contact.query.filter_by(username=username).first()
    if contact:
        contact.update_from_dict(**data)
        contact.delete_emails()
        for email in data['emails']:
            contact.email.append(Email(email=email))
        save_changes(contact)
        return contact, 200
    return False, 'contact not found'


def delete_contact(username):
    contact = Contact.query.filter_by(username=username).first()
    if contact:
        delete_object(contact)
        response_object = {
            'status': 'success',
            'message': 'Contact successfully deleted.'
        }
        return response_object, 200
    return False, 'contact not found'


def save_changes(data):
    """ helper for saving into db """
    db.session.add(data)
    db.session.commit()


def delete_object(db_object):
    """ helper for deleting from db"""
    db.session.delete(db_object)
    db.session.commit()
