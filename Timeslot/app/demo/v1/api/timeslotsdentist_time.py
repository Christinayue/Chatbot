# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from flask import request, g, make_response, jsonify
from . import Resource
from .. import schemas
import ast


class TimeslotsdentistTime(Resource):
    def get(self, time):
        result = []
        tempP = " "
        print(time)
        j = 0
        with open('dentists.txt', 'r+') as f:
            for line in f:
                if not line.strip():
                    continue
                line = ast.literal_eval(line)
                #print(line['time'].split()[0])
                if line['time'].split()[0]== time and line['status'] == 'available':
                    j +=1
                    tempP +="******"+str(j) + ". " + "\n"
                    for i in line:
                        tempP += i + ": " + str(line[i]) + ",  "
                    result.append(line)
                    print(result)
        f.close()
        if result == []:
            return make_response(jsonify(message='wrong dentist name'), 200)
        return make_response(jsonify(message=tempP), 200)
        