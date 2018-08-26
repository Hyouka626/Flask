#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Hyouka

from waitress import serve
from app import app,socketio


if __name__ == '__main__':
    serve(socketio.run(app, host='0.0.0.0', port=8080))
