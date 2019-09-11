# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.ask_message import AskMessage


routes = [
    dict(resource=AskMessage, urls=['/ask/<message>'], endpoint='ask_message'),
]