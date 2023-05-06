# coding: utf-8
"""
Abstract::
	- 
History::
	- Ver.      Date            Author        History
	- 
"""
# 標準ライブラリ
from http import HTTPStatus

# 関連外部ライブラリ
from flask import Blueprint, jsonify, request
# import app
from services.ws_service import SocketclusterClient


# インスタンス
publish_route = Blueprint("model", __name__, url_prefix="/publish")

# ==============================================================================
# API FUNCTION
# ==============================================================================
@publish_route.route("/", methods=["GET"])
def retrieve_model_names():
	"""
	Retrieve all model names from engine 
	"""
	try:
		print('subribe_channel')

		SocketclusterClient().publish_via_channel(channel='yell', content='ok')

		content = {"success": 'ok'}

		status = HTTPStatus.OK

	except Exception as exception:
		content = {"error": str(exception)}

		status = HTTPStatus.INTERNAL_SERVER_ERROR

	return jsonify(content), status


