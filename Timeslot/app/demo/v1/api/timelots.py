# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from flask import request, g, make_response, jsonify
from . import Resource
from .. import schemas
import ast

class Timelots(Resource):
    def get(self):
        result = []
        with open('dentists.txt', 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                result.append(line)
        f.close()
        s = []
        for e in result:
            e = ast.literal_eval(e)
            if e['status']== 'available':
                s.append(e)
        print(s)
        return s, 200, None

   