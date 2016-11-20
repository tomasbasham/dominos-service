dominos-proxy |build|
=====================

.. |build| image:: https://travis-ci.org/tomasbasham/dominos-proxy.svg?branch=master
    :target: https://travis-ci.org/tomasbasham/dominos-proxy

A Python `Flask <http://flask.pocoo.org/>`_ Dominos Pizza UK proxy service
using the `dominos <https://github.com/tomasbasham/dominos>`_ library.

Installation
------------

Installing the latest version from Github:

.. code:: bash

    $ git clone https://github.com/tomasbasham/dominos-proxy
    $ cd dominos-proxy
    $ pip install -r requirements.txt

Usage
-----

.. code:: bash

    $ gunicorn server:app -c config/gunicorn.py

Visit your app at `http://localhost:5000 <http://localhost:5000>`_.

Deploying
---------

For simple deployment without having to checkout this repository you can deploy
to `heroku <https://www.heroku.com/>`_ using the 'Deploy to Heroku' button
below.

.. image:: https://www.herokucdn.com/deploy/button.png
   :alt: Deploy to Heroku
   :target: https://heroku.com/deploy

Contributing
------------

1. Fork it (https://github.com/tomasbasham/dominos-proxy/fork)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
