# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g,make_response, jsonify

from . import Resource
from .. import schemas
import ast

class DentistsName(Resource):

    def get(self, name):
        result = []
        with open('dentists.txt', 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                result.append(line)
        f.close()
        #print(result)
        s = []
        tempP = " "
        for e in result:
            e = ast.literal_eval(e)
            if e['name'] == name:
                for i in e:
                    tempP += i + ": " + str(e[i]) + ", "
                print(e)
                s = e
        return make_response(jsonify(message=tempP),200)