"""
Simple job implementations clock-based.
"""
import datetime
from logging import info

from jobs import app


@app.on_after_configure.connect
def start_task_at_beat(sender, **kwargs):
    """
    Execute a job periodically 
    """
    sender.add_periodic_task(3, execute_job.s(), name="Say what time is now")


@app.task(name='clock-based_simple_job')
def execute_job():
    """
    Logging a msg
    """
    moment = datetime.datetime.now()
    info(f'Executado agora @[{moment.strftime("%d/%m/%Y %H:%M:%S")}]')
    return moment
