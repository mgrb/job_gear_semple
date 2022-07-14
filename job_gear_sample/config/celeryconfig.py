"""
Celery basic configuration based on definition described at: 
https://docs.celeryq.dev/en/stable/userguide/configuration.html#example-configuration-file
"""
import os
from dotenv import load_dotenv
load_dotenv()

broker_url = os.environ.get('CELERY_BROKER_URL')
result_backend = os.environ.get('CELERY_RESULT_BECKEND')
task_always_eager = os.environ.get('CELERY_ALWAYS_EAGER')

# Register all jobs class implementation into the following array
imports = ['jobs.ondemand_simple_job']
