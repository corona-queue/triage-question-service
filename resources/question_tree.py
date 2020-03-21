from flask_restful import Resource


class QuestionTreeResource(Resource):
    def get(self):
        return {'hello': 'world'}
