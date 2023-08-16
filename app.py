from flask import request, make_response
from flask_restful import Resource

from config import api, app, db
from models import Show, Blog

class Home(Resource):

    def get(self):
        return 'mahalo'
    
class Shows(Resource):
    def get(self):
        try:
            shows = [s.to_dict() for s in Show.query.all()]

            response = make_response(shows, 200)
            return response
        except Exception as e:
            response = make_response(e, 500)
            return response
    
class Blogs(Resource):
    def get(self):
        try:
            blogs = [b.to_dict() for b in Blog.query.all()]

            response = make_response(blogs, 200)
            return response
        except Exception as e:
            response = make_response(e, 500)
            return response
    
    def post(self):
        try:
            data = request.get_json()
            title = data.get('title')
            content = data.get('content')

            if not title or not content:
                response = make_response("error': 'Title and content are required fields.", 400)
                return response
            
            new_blog_post = Blog(title=title, content=content)
            db.session.add(new_blog_post)
            db.session.commit()

            response = make_response('Blog posted!', 201)
            return response
        
        except Exception as e:
            response = make_response(e, 500)
            return response

api.add_resource(Home, '/')
api.add_resource(Shows, '/shows')
api.add_resource(Blogs, '/blogs')

if __name__ == '__main__':
    app.run(port=5555, debug=True)