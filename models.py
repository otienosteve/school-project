from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# postgres://school_fsnx_user:yVp7USuV5INATh8WGcQ0KmguT5C9dcPl@dpg-cml3av7109ks73a5ad90-a.oregon-postgres.render.com/school_fsnx
db = SQLAlchemy()
class User(db.Model, SerializerMixin):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

class TokenBlocklist(db.Model):
    __tablename__ ='token_blocklist'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)


class Teacher(db.Model,SerializerMixin):
    serialize_rules = ('-departments.teacher',)
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    departments = db.relationship('Department', backref = 'teacher')

class Department(db.Model, SerializerMixin):
    __tablename__ = 'departments'
    code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

class Course(db.Model, SerializerMixin):
    __tablename__ = 'courses'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    photo_url = db.Column(db.String(50))
    pass_mark = db.Column(db.Integer)