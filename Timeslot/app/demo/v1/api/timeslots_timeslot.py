# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from flask import request, g, make_response, jsonify
from . import Resource
from .. import schemas
import ast


class TimeslotsTimeslot(Resource):

    def get(self, timeslot):
        result = []
        with open('dentists.txt', 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                result.append(line)
        f.close()
        s = []
        tempP = " "
        for e in result:
            e = ast.literal_eval(e)
            if e['id']== timeslot:
                for i in e:
                    tempP += i + ": " + str(e[i]) + ",  "
                tempP += " .     "
                s.append(e)
        print(s)
        if s == []:
            return make_response(jsonify(message='wrong timeslot number'), 400)
        return make_response(jsonify(message=tempP),200)

    def post(self, timeslot):
        print(timeslot)
        result = []
        p = []
        
        tempP = " "
        with open('dentists.txt', 'r+') as f:
            for line in f:
                if not line.strip():
                    continue
                line = ast.literal_eval(line)
                #print(line['time'])
                if line['id'] == timeslot:       
                    if line['status'] == 'available':
                        before = line
                        line['status']= 'booked'
                        for i in line :
                            tempP += i + ": " + str(line[i]) + ",  "
                        tempP += ".    "
                        print(tempP)    
                        p = line
                        #print(line)
                    else:
                        return make_response(jsonify(message = 'This timeslot booked.'),400)
                result.append(line)
            #print(p,before)     
        f.close()
        f = open('dentists.txt', 'w')
        for i in result:
            f.write(str(i))
            f.write("\n")
        f.close()
        if p == []:
            return make_response(jsonify(message= 'Wrong information, you need correct name or id or time'), 400)
        return make_response(jsonify(message=tempP), 200)

    

    def delete(self, timeslot):
        result = []
        p = []
        tempP = " "
        with open('dentists.txt', 'r+') as f:
            for line in f:
                if not line.strip():
                    continue
                line = ast.literal_eval(line)
                if line['id'] == timeslot:
                    line['status'] = 'available'
                    p = line
                    for i in line:
                        tempP += i + ": " + str(line[i]) + " , "
                    tempP += " .     "
                result.append(line)
        f.close()
        print(result)
        f = open('dentists.txt', 'w')
        for i in result:
            f.write(str(i))
            f.write("\n")
        f.close()
        if p == []:
            return make_response(jsonify(message='wrong timeslot number'), 400)
        return  make_response(jsonify(message=tempP), 200)