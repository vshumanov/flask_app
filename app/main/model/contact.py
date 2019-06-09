from .. import db


class Contact(db.Model):
    """ Contact Model for storing contact related details """
    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    # created_at = db.Column(db.DateTime, nullable=False)

    email = db.relationship(
        "Email", back_populates="contact", cascade="all, delete-orphan")

    def update_from_dict(self, **kwargs):
        """ updates the model with dict """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def delete_emails(self):
        for email in self.email:
            db.session.delete(email)

    def as_dict(self):
        return {'username': self.username,
                'first_name': self.first_name,
                'surname': self.surname,
                'emails': [x.email for x in self.email]
                }

    def __repr__(self):
        return f'<User {self.username}, {self.first_name}, {self.surname}>'

    def __eq__(self, other):
        """Override the default Equals behavior for testing purposes"""
        return self.email == other.email and self.username == other.username \
            and self.first_name == other.first_name and self.surname == other.surname
