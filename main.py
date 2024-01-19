from flask import Blueprint, request, make_response, jsonify

from flask_restful import Resource, Api, reqparse , abort
from flask_marshmallow import Marshmallow
from flask_jwt_extended import jwt_required


from models import db,Teacher, Department, Course, User
main_bp = Blueprint('main',__name__)



api = Api(main_bp) 
ma = Marshmallow(main_bp)





class DepartmentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Department
    code = ma.auto_field()
    name = ma.auto_field()
    
class TeacherSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Teacher
    id = ma.auto_field()
    name = ma.auto_field()
    departments = ma.Nested(DepartmentSchema, many=True)

teacher_schema = TeacherSchema()



def collapse():
    # @app.route('/')
    # def index():
    #     return {"msg" :"Modified Index Route"} 

    # @app.route('/home/<string:name>')
    # def home(name):
    #     return {"detail": f"Welcome home {name}"}

    # @app.route('/square/<int:num>')
    # def square(num):
    #     return str(num*num)

    # @app.route('/teacher/<int:id>', methods=['GET','PATCH','DELETE'])
    # def teacher(id):
    #     teacher_one = Teacher.query.filter_by(id=id).first()
    #     if not teacher_one:
    #         return make_response(jsonify({"detail":f"teacher with id {id} does not exist"}), 404)

    #     if request.method == 'GET':
    #         response = teacher_one.to_dict()
    #         return response

    #     if request.method == 'PATCH':
    #         for key,value in  request.get_json().items():
    #             setattr(teacher_one, key, value)
    #         db.session.commit() 
    #         return teacher_one.to_dict()

    #     if request.method =='DELETE':
    #         db.session.commit()
    #         return {"detail": f"teacher with if {id} has been deleted successfully"}

    # @app.route('/add_teacher', methods=['POST'])
    # def add_teacher():
    #     teacher = Teacher(**request.get_json())
    #     db.session.add(teacher)
    #     db.session.commit()
    #     return teacher.to_dict()

    # # @app.get(), .post()
    # @app.route('/teachers')
    # def all_teachers():
    #     teachers = Teacher.query.all()
    #     response =[]
    #     for teacher in teachers:
    #         response.append(teacher.to_dict())
    #     # print(response)
    #     return response
    pass

patch_args = reqparse.RequestParser(bundle_errors= True)
patch_args.add_argument('id',type=int,help='Id of the Teacher')
patch_args.add_argument('name',type=str,help='Name of the Teacher')

post_args = reqparse.RequestParser(bundle_errors= True)
post_args.add_argument('id',type=int,help='Add Id of the Teacher', required = True)
post_args.add_argument('name',type=str,help='Add Name of the Teacher', required = True)





class Example(Resource):
    

    def get(self):
        return {"mgs":"This is Flask Restful"}

    def patch(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

teachers_schema = TeacherSchema(many=True)
class TeacherResource(Resource):
    
    def get(self):
        teachers = Teacher.query.all()
        return teachers_schema.dump(teachers) 
    
    def post(self):
        data = post_args.parse_args()
        new_teacher = Teacher(**data)
        db.session.add(new_teacher)
        db.session.commit()
        return new_teacher.to_dict()
teacher_schema = TeacherSchema()
class TeacherById(Resource):

    @jwt_required()
    def get(self, id):
        teacher = Teacher.query.filter_by(id=id).first()
        return teacher_schema.dump(teacher)
    
    def patch(self, id):
        teacher = Teacher.query.filter_by(id=id).first()
        data = patch_args.parse_args()
        print(data)
        for key,value in data.items():
            if value is None:
                continue
            setattr(teacher,key,value)
        db.session.commit()
        return teacher.to_dict()

    def delete(self, id):
        Teacher.query.filter_by(id=id).delete()
        db.session.commit()
        return {"detail":f"Teacher with id {id} has been deleted successfully"}


api.add_resource(Example,'/example')
api.add_resource(TeacherResource,'/teachers')
api.add_resource(TeacherById,'/teacher/<int:id>')

