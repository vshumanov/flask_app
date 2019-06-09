from .. import db


class Email(db.Model):
    """ Email Model for storing contact emails """
    __tablename__ = 'email'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    contact = db.relationship('Contact', back_populates='email')

    def __repr__(self):
        return f'<Email {self.email}, contact_id {self.contact_id}>'
