import datetime as dt
from marshmallow import Schema, fields, post_load
from app import db


class Dog(db.Model):
    """
    Dog model class
        args:
            name: str
            image: str
            description: str
            created_at: datetime
    """
    __tablename__ = 'dogs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    image = db.Column(db.String(255))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, name, image, description) -> None:
        self.name = name
        self.image = image
        self.description = description
        self.created_at = dt.datetime.now()

    def __repr__(self) -> str:
        return f'Dog(name={self.name}, image={self.image}, description={self.description}, created_at={self.created_at})'


class DogSchema(Schema):
    name = fields.Str()
    image = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()

    @post_load
    def make_dog(self, data, **kwargs):
        return Dog(**data)
