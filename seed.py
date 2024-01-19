from models import db, Teacher
from main import app 

teachers = [{
  "id": 1,
  "name": "Marty"
}, {
  "id": 2,
  "name": "Ealasaid"
}, {
  "id": 3,
  "name": "Eolanda"
}, {
  "id": 4,
  "name": "Broderick"
}, {
  "id": 5,
  "name": "Farr"
}, {
  "id": 6,
  "name": "Flint"
}, {
  "id": 7,
  "name": "Annmarie"
}, {
  "id": 8,
  "name": "Audie"
}, {
  "id": 9,
  "name": "Keeley"
}, {
  "id": 10,
  "name": "Myrtia"
}]

with app.app_context():
    db.session.add_all([Teacher(**teacher) for teacher in teachers])
    db.session.commit()
