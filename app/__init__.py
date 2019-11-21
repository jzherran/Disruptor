# app.py or app/__init__.py
import os

from flask import Flask

def create_app(test_config=None):
  """Create and configure an instance of the Disruptor application."""
  app = Flask(__name__, instance_relative_config=True)
  # load configuration for instance and general file
  app.config.from_object('config')
  app.config.from_pyfile('config.py')

  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  @app.route("/hello")
  def hello():
    return "Hello, World!"

  return app