""" サービスのログ出力をサポート

サービスのログ出力をサポートするロギング用のライブラリ

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


def doktor_logging(func):
    def _wrapper(*args, **kwargs):
        # before
        func(*args, **kwargs)
        # after

    return _wrapper