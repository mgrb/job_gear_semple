"""
Initialize a Celery app.
"""
from celery import Celery
from config import celeryconfig


def make_celery():
    """
    Link the JOBs with a celery broker.
    """
    celery = Celery(__name__)
    celery.config_from_object(celeryconfig)
    return celery


app = make_celery()
