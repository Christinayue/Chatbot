# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from flask import request, g, make_response, jsonify
from . import Resource
from .. import schemas
import ast

class DentistDentist(Resource):
    def get(self, dentist):
        result = []
        tempP = ""
        j = 0
        with open('dentists.txt', 'r+') as f:
            for line in f:
                if not line.strip():
                    continue
                line = ast.literal_eval(line)
                if line['name'] == dentist and line['status'] == 'available':
                    j +=1
                    tempP += "******" + str(j) + ". "
                    for i in line:
                        tempP += i + ": " + str(line[i]) + ",    "
                    result.append(line)
        f.close()
        if result == []:
            return make_response(jsonify(message='wrong dentist name'), 200)
        return make_response(jsonify(message=tempP), 200)