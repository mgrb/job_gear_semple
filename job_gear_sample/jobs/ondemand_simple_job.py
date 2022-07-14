"""
Implementation of a 'on demand' job.
"""
from logging import info

from jobs import app


@app.task(name='on_demand_job')
def add(arg01: int, arg02: int):
    """
    it receives 2 arguments and return a sum of them.
    """
    info('Chamado SOMAR...')
    # time.sleep(5)
    result = arg01 + arg02
    info(f'O Resultado foi = {result}')
    return result
