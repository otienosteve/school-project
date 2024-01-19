from flask import Blueprint, request 
from flask_marshmallow import Marshmallow 
from flask_restful import Resource, Api, reqparse, abort


from models import db, Course
from flask_jwt_extended import jwt_required

course_bp = Blueprint('course_blueprint',__name__)
ma = Marshmallow(course_bp)
api = Api(course_bp)

patch_args = reqparse.RequestParser(bundle_errors= True)
patch_args.add_argument('name', type=str, help="add name of the course") 
patch_args.add_argument('photo_url', type=str, help="add photo_url of the course") 
patch_args.add_argument('pass_mark', type=int, help="add pass_mark of the course") 

class CourseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Course
    id = ma.auto_field()
    name = ma.auto_field()
    photo_url =ma.auto_field()
    pass_mark = ma.auto_field()


#all courses
courses_schema = CourseSchema(many = True)
course_schema = CourseSchema()

class CourseRs(Resource):

    @jwt_required()
    def get(self):
        courses = Course.query.all()
        return courses_schema.dump(courses)
    
    @jwt_required()
    def post(self):
        new_course = Course(**request.json)
        db.session.add(new_course)
        db.session.commit()
        return course_schema.dump(new_course)

    
class CourseByID(Resource):

    # @staticmethod
    # def getInstance(id):
    #     return Course.query.get(id)
    @jwt_required()
    def patch(self, id):
        course = Course.query.get(id)
        data = patch_args.parse_args()

        for key,value in data.items():
            if value is None:
                continue
            setattr(course,key,value)
        db.session.commit()
        return course_schema.dump(course)

        
    @jwt_required()
    def get(self, id):
        course = Course.query.get(id)
        if not course:
            abort(404, detail="Course does not exist")
        return course_schema.dump(course)
    
    @jwt_required()
    def delete(self, id):
        Course.query.filter_by(id=id).delete()
        db.session.commit()
        return {"detail": f"User with {id=} has been deleted successfully"}


    
api.add_resource(CourseRs,'/courses')
api.add_resource(CourseByID,'/courses/<int:id>')




# @course_bp.route('/courses', methods = ['GET', 'POST'])
# def course():
#     if request.method == 'GET':
#         courses = Course.query.all()
#         # response = [course.to_dict() for course in courses]
#         return course_schema.dump(courses)
    # if request.method == 'POST':
    #     new_course = Course(**request.json)
    #     db.session.add(new_course)
    #     db.session.commit()
    #     return new_course.to_dict()

#creating a course

# @course_bp.route()

# deleting a course


# updating a course 