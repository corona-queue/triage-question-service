from flask import Flask
from flask_restful import Api
from resources.question_tree import QuestionTreeResource

app = Flask(__name__)
api = Api(app)

api.add_resource(QuestionTreeResource, '/api/question-tree')

if __name__ == '__main__':
    app.run(debug=True)
