from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

from config import db

class Show(db.Model, SerializerMixin):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    venue = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(64), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    link = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Show {self.id}: Live at {self.venue} on {self.date}'
    
class Blog(db.Model, SerializerMixin):
    __tablename__ = 'blog_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'Blog Post {self.id}: {self.title} published on {self.timestamp}'

