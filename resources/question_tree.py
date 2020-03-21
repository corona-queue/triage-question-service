import json
from flask_restful import Resource


class QuestionTreeResource(Resource):
    def get(self):
        question_json = {}
        with open('files/questions.json') as json_file:
            question_json = json.load(json_file)
        # TODO: Build Mapping from keys on concrete texts
        print(question_json)
        return question_json
