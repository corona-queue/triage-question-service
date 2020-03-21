import json
from flask_restful import Resource, reqparse
from utils.english_text_mapping import english_text_map
from utils.german_text_mapping import german_text_map


text_maps = {"eng": english_text_map, "ger": german_text_map}


class QuestionTreeResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lang', type=str)

        args = parser.parse_args()

        active_text_map = text_maps[args["lang"]]

        question_json = {}
        with open('files/questions.json') as json_file:
            question_json = json.load(json_file)

        # Translate text for answers
        option_results = []
        for option in question_json["options"]:
            option_results.append(active_text_map[option])
        question_json["options"] = option_results

        # Translate text for question
        text_id = question_json["text"]
        text_id["text"] = active_text_map[text_id]

        return question_json
