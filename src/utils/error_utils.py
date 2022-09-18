from flask import jsonify


class ErrorUtils:
    @staticmethod
    def raise_not_found(obj="Object"):
        return jsonify({"error": "{} not found".format(obj)}), 404
