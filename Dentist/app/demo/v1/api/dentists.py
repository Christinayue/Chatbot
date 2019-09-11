# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from flask import request, g, make_response, jsonify
from . import Resource
from .. import schemas
import ast

class Dentists(Resource):

    def get(self):
        result = []
        with open('dentists.txt', 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                result.append(line)
        f.close()
        s = []
        tempP = " "
        j = 0
        for e in result:
            e = ast.literal_eval(e)
            j += 1
            tempP += "******" + str(j) + ". "
            for i in e:
                print(e[i])
                tempP += i + ": " + str(e[i]) + ",   "
            s.append(e)
        #print(s)
        return make_response(jsonify(message=tempP),200)

    def post(self):
        print(g.json)
        na = g.json['name']
        phone = g.json['phone']
        location = g.json['location']
        spe = g.json['specializaton']
        time = g.json['time']
        f = open("dentists.txt", "a")
        f.write(str(g.json))
        f.write("\n")
        f.close()
        return make_response(jsonify(name=na),200) 