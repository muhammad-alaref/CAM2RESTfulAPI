"""Provides user authentication

This module provides simple user
authentication based on the HTTP
Basic access authentication method

Based on a code snippet from http://flask.pocoo.org/snippets/8/

"""

from functools import wraps
from flask import request, Response
from werkzeug.security import check_password_hash
from CAM2RESTfulAPI import database_client

def check_auth(username, password):
	"""This function is called to check if a username-password combination is valid.
	"""
	return check_password_hash(database_client.query_db('SELECT * FROM Users WHERE username=?', args=(username,), one=True)['password_hash'], password)

def authenticate():
	"""Sends a 401 response that enables basic auth"""
	return Response(
		'Could not verify your access level for that URL.\n'
		'You have to login with proper credentials', 401,
		{'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
	'''Provides authentication as a simple decorator'''
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			return authenticate()
		return f(*args, **kwargs)
	return decorated 
