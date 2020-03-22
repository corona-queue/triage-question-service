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

        language = args["lang"] or "ger"

        active_text_map = text_maps[language]

        question_json = {}
        with open('files/questions.json') as json_file:
            question_json = json.load(json_file)

        for question in question_json:
            # Translate text for answers
            if question["options"]:
                option_results = []
                for index, option in enumerate(question["options"]):
                    value = 0
                    if "scoreMap" in question:
                        value = question["scoreMap"][index]
                    option_results.append({'id': option,
                                           'text': active_text_map[option],
                                           'value': value})
                question["options"] = option_results

            if "comment" in question and question["comment"]:
                comment_id = question["comment"]
                question["comment"] = active_text_map[comment_id]

            # Translate text for question
            text_id = question["text"]
            question["text"] = active_text_map[text_id]

        return question_json
