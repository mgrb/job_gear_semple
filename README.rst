Preparing the environment
====
#. poetry shell
#. poetry install

RabbitMQ
----

.. code-block::

    $ docker run -d --hostname ceq_mq --name rabbitMQ -p 15672:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=cer_user -e RABBITMQ_DEFAULT_PASS=Qwert123 rabbitmq:3-management

Start beat worker
----
.. code-block::

    $ celery -A jobs.clockbased_simple_job beat --loglevel=info